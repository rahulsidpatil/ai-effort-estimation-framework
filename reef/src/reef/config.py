"""Environment-backed application settings."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from reef import __version__


@dataclass(frozen=True, slots=True)
class Settings:
    """Runtime settings kept deliberately small for the Step 0 application."""

    environment: str
    application_version: str
    log_level: str
    data_dir: Path
    database_path: Path

    @classmethod
    def from_environment(cls) -> Settings:
        data_dir = Path(os.getenv("REEF_DATA_DIR", ".reef-data")).expanduser()
        database_path = Path(
            os.getenv("REEF_DATABASE_PATH", str(data_dir / "reef.db"))
        ).expanduser()
        return cls(
            environment=os.getenv("REEF_ENVIRONMENT", "development"),
            application_version=os.getenv("REEF_VERSION", __version__),
            log_level=os.getenv("REEF_LOG_LEVEL", "INFO").upper(),
            data_dir=data_dir,
            database_path=database_path,
        )
