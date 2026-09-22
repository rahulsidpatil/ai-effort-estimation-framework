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
    assert 'href="/product-experience"' in page.text
    assert "content-security-policy" in page.headers
    assert health.json()["status"] == "ok"
    assert health.json()["version"] == "test-version"
    assert health.headers["x-request-id"]
    assert readiness.status_code == 200
    assert readiness.json() == {"status": "ready"}


def test_product_experience_is_an_explicit_local_simulation(tmp_path: Path) -> None:
    with TestClient(create_app(settings_for(tmp_path))) as client:
        response = client.get("/product-experience")
        javascript = client.get("/static/product-experience.js")

    assert response.status_code == 200
    assert response.text.count("data-stage-panel=") == 10
    assert response.text.count("data-stage-target=") == 10
    assert 'id="tourOverview"' in response.text
    assert "What REEF does" in response.text
    assert "what this tour demonstrates" in response.text.lower()
    assert "Start with the project brief" in response.text
    assert "Explore all 10 stages" in response.text
    assert "does not calculate or save a real estimate" in response.text
    assert "Estimation lead" in response.text
    assert "Commercial lead" in response.text
    assert "Not an employee score" in response.text
    assert "Not a computed estimate" in response.text
    assert "never submitted" in response.text
    assert "Clear local copy" in response.text
    assert "script-src 'self'" in response.headers["content-security-policy"]
    assert "form-action 'none'" in response.headers["content-security-policy"]
    assert javascript.status_code == 200
    assert "reef-product-experience-feedback" in javascript.text
    assert "fetch(" not in javascript.text


def test_readiness_fails_when_database_disappears(tmp_path: Path) -> None:
    settings = settings_for(tmp_path)
    with TestClient(create_app(settings)) as client:
        settings.database_path.unlink()
        response = client.get("/readyz")

    assert response.status_code == 503
    assert response.json() == {"status": "not_ready"}
