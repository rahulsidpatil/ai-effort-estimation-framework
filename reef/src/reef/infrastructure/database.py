"""SQLite lifecycle and readiness operations."""

from __future__ import annotations

import sqlite3
from pathlib import Path


def initialize_database(database_path: Path) -> None:
    """Create the Step 0 database and its metadata table if necessary."""
    database_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(database_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS reef_metadata (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )
            """
        )
        connection.execute(
            "INSERT OR IGNORE INTO reef_metadata (key, value) VALUES (?, ?)",
            ("database_schema_version", "0"),
        )


def database_is_ready(database_path: Path) -> bool:
    """Return whether the configured SQLite database can answer a query."""
    try:
        with sqlite3.connect(f"file:{database_path}?mode=rw", uri=True) as connection:
            row: tuple[int] | None = connection.execute("SELECT 1").fetchone()
    except (OSError, sqlite3.Error):
        return False
    return row == (1,)
