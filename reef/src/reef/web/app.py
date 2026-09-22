"""FastAPI application factory for the REEF Step 0 deployment."""

from __future__ import annotations

import logging
import time
import uuid
from collections.abc import AsyncIterator, Awaitable, Callable
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import Response

from reef.config import Settings
from reef.infrastructure.database import database_is_ready, initialize_database
from reef.web.logging import configure_logging

LOGGER = logging.getLogger("reef.web")
WEB_ROOT = Path(__file__).parent


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create an isolated application instance for runtime or testing."""
    runtime_settings = settings or Settings.from_environment()
    configure_logging(runtime_settings.log_level)

    @asynccontextmanager
    async def lifespan(_: FastAPI) -> AsyncIterator[None]:
        initialize_database(runtime_settings.database_path)
        LOGGER.info("REEF started")
        yield
        LOGGER.info("REEF stopped")

    app = FastAPI(
        title="REEF API",
        summary="Reusable Effort Estimation Framework reference application",
        version=runtime_settings.application_version,
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        lifespan=lifespan,
    )
    app.state.settings = runtime_settings
    app.mount("/static", StaticFiles(directory=WEB_ROOT / "static"), name="static")
    templates = Jinja2Templates(directory=WEB_ROOT / "templates")

    @app.middleware("http")
    async def operational_middleware(
        request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        request_id = uuid.uuid4().hex
        started = time.perf_counter()
        response = await call_next(request)
        duration_ms = round((time.perf_counter() - started) * 1000, 2)
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; style-src 'self'; img-src 'self'; frame-ancestors 'none'"
        )
        LOGGER.info(
            "HTTP request completed",
            extra={
                "method": request.method,
                "path": request.url.path,
                "status_code": response.status_code,
                "duration_ms": duration_ms,
                "request_id": request_id,
            },
        )
        return response

    @app.get("/", response_class=HTMLResponse, include_in_schema=False)
    async def index(request: Request) -> HTMLResponse:
        return templates.TemplateResponse(
            request=request,
            name="index.html",
            context={
                "environment": runtime_settings.environment,
                "version": runtime_settings.application_version,
            },
        )

    @app.get("/healthz", tags=["operations"])
    async def health() -> dict[str, str]:
        return {"status": "ok", "version": runtime_settings.application_version}

    @app.get("/readyz", tags=["operations"])
    async def readiness() -> JSONResponse:
        if database_is_ready(runtime_settings.database_path):
            return JSONResponse({"status": "ready"})
        return JSONResponse(
            {"status": "not_ready"},
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        )

    return app


app = create_app()
