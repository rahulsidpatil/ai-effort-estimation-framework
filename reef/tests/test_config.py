from pathlib import Path

import pytest

from reef.config import Settings


def test_settings_use_environment(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setenv("REEF_ENVIRONMENT", "test")
    monkeypatch.setenv("REEF_VERSION", "1.2.3")
    monkeypatch.setenv("REEF_LOG_LEVEL", "debug")
    monkeypatch.setenv("REEF_DATA_DIR", str(tmp_path))

    settings = Settings.from_environment()

    assert settings.environment == "test"
    assert settings.application_version == "1.2.3"
    assert settings.log_level == "DEBUG"
    assert settings.database_path == tmp_path / "reef.db"
