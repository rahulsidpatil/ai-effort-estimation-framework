from pathlib import Path

from reef.infrastructure.database import database_is_ready, initialize_database


def test_database_lifecycle(tmp_path: Path) -> None:
    database_path = tmp_path / "nested" / "reef.db"

    assert database_is_ready(database_path) is False
    initialize_database(database_path)
    assert database_is_ready(database_path) is True
