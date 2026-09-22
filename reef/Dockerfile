# syntax=docker/dockerfile:1.7@sha256:a57df69d0ea827fb7266491f2813635de6f17269be881f696fbfdf2d83dda33e
FROM python:3.12-slim@sha256:2f17fc044b579bab302c2e8054d3a686e2cb9a83de48e70534b94cd8ebbe06a9 AS builder

ARG UV_VERSION=0.11.30
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy
WORKDIR /app

RUN python -m pip install --no-cache-dir "uv==${UV_VERSION}"
COPY pyproject.toml uv.lock README.md ./
COPY src ./src
RUN uv sync --frozen --no-dev --no-editable

FROM python:3.12-slim@sha256:2f17fc044b579bab302c2e8054d3a686e2cb9a83de48e70534b94cd8ebbe06a9 AS runtime

ARG REEF_VERSION=0.1.0.dev0
LABEL org.opencontainers.image.title="REEF" \
      org.opencontainers.image.description="Reusable Effort Estimation Framework reference web application" \
      org.opencontainers.image.licenses="Apache-2.0" \
      org.opencontainers.image.version="${REEF_VERSION}" \
      org.opencontainers.image.source="https://github.com/rahulsidpatil/ai-effort-estimation-framework"

ENV PATH="/app/.venv/bin:${PATH}" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    REEF_VERSION="${REEF_VERSION}" \
    REEF_DATA_DIR=/data \
    REEF_ENVIRONMENT=container \
    REEF_LOG_LEVEL=INFO

RUN groupadd --gid 10001 reef \
    && useradd --uid 10001 --gid reef --no-create-home --shell /usr/sbin/nologin reef \
    && mkdir -p /data \
    && chown reef:reef /data

WORKDIR /app
COPY --from=builder --chown=reef:reef /app/.venv /app/.venv

USER 10001:10001
EXPOSE 8000
VOLUME ["/data"]
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
  CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/readyz', timeout=2)"]

ENTRYPOINT ["uvicorn"]
CMD ["reef.web.app:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
