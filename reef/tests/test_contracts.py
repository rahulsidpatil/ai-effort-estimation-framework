import json
from pathlib import Path
from typing import Any

import pytest
import yaml
from jsonschema import Draft202012Validator, FormatChecker

REPOSITORY_ROOT = Path(__file__).parents[2]

CONTRACTS = (
    ("schemas/project.schema.json", "examples/projects/example-project.yaml"),
    ("schemas/estimate.schema.json", "examples/estimates/example-estimate.json"),
    ("schemas/actuals.schema.json", "examples/observations/example-actuals.yaml"),
)


def load_document(path: Path) -> Any:
    with path.open(encoding="utf-8") as document:
        if path.suffix == ".json":
            return json.load(document)
        return yaml.safe_load(document)


@pytest.mark.parametrize(("schema_name", "example_name"), CONTRACTS)
def test_public_example_conforms_to_schema(schema_name: str, example_name: str) -> None:
    schema = load_document(REPOSITORY_ROOT / schema_name)
    example = load_document(REPOSITORY_ROOT / example_name)

    Draft202012Validator(schema, format_checker=FormatChecker()).validate(example)
