import json
from pathlib import Path


def load_metadata(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def extract_metadata_fields(data):
    return {
        "id": data.get("id"),
        "title": data.get("title"),
        "module": data.get("module"),
        "order": data.get("order"),
        "concepts": data.get("concepts", []),
    }


def validate_required_fields(data, required_fields):
    return [field for field in required_fields if field not in data]
