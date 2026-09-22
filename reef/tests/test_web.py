from pathlib import Path

from fastapi.testclient import TestClient

from reef.config import Settings
from reef.web.app import create_app


def settings_for(tmp_path: Path) -> Settings:
    return Settings(
        environment="test",
        application_version="test-version",
        log_level="WARNING",
        data_dir=tmp_path,
        database_path=tmp_path / "reef.db",
    )


def test_browser_and_operational_endpoints(tmp_path: Path) -> None:
    with TestClient(create_app(settings_for(tmp_path))) as client:
        page = client.get("/")
        health = client.get("/healthz")
        readiness = client.get("/readyz")

    assert page.status_code == 200
    assert "delivery foundation is ready" in page.text
    assert "content-security-policy" in page.headers
    assert health.json()["status"] == "ok"
    assert health.json()["version"] == "test-version"
    assert health.headers["x-request-id"]
    assert readiness.status_code == 200
    assert readiness.json() == {"status": "ready"}


def test_readiness_fails_when_database_disappears(tmp_path: Path) -> None:
    settings = settings_for(tmp_path)
    with TestClient(create_app(settings)) as client:
        settings.database_path.unlink()
        response = client.get("/readyz")

    assert response.status_code == 503
    assert response.json() == {"status": "not_ready"}
