import json
import os
import sys

CONTENT_DIR = "content"
METADATA_DIR = "metadata"
SCHEMA_PATH = os.path.join(METADATA_DIR, "schema.json")

REQUIRED_FIELDS = {
    "id": str,
    "title": str,
    "module": str,
    "order": (int, float),
    "concepts": list,
}


def find_files(base_dir: str, extension: str):
    paths = []
    if not os.path.exists(base_dir):
        return paths

    for root, _, files in os.walk(base_dir):
        for name in files:
            if name.endswith(extension):
                paths.append(os.path.join(root, name))

    return paths


def load_schema():
    if not os.path.exists(SCHEMA_PATH):
        return None

    with open(SCHEMA_PATH, "r", encoding="utf-8") as schema_file:
        return json.load(schema_file)


def validate_metadata_types(data, metadata_path):
    errors = []

    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in data:
            errors.append(f"Falta campo '{field}' en {metadata_path}")
            continue

        value = data[field]
        if not isinstance(value, expected_type):
            errors.append(
                f"Tipo inválido para '{field}' en {metadata_path}: "
                f"esperado {expected_type}, recibido {type(value)}"
            )

    if isinstance(data.get("concepts"), list):
        invalid_items = [item for item in data["concepts"] if not isinstance(item, str)]
        if invalid_items:
            errors.append(
                f"Todos los elementos de 'concepts' deben ser string en {metadata_path}"
            )

    return errors


def validate_against_schema(data, schema, metadata_path):
    errors = []

    if not schema:
        return errors

    for field in schema.keys():
        if field not in data:
            errors.append(f"No cumple schema: falta '{field}' en {metadata_path}")

    return errors


def validate_structure():
    errors = []

    md_files = find_files(CONTENT_DIR, ".md")
    json_files = [
        path
        for path in find_files(METADATA_DIR, ".json")
        if os.path.basename(path) != "schema.json"
    ]

    md_by_base = {
        os.path.splitext(os.path.basename(path))[0]: path
        for path in md_files
    }
    json_by_base = {
        os.path.splitext(os.path.basename(path))[0]: path
        for path in json_files
    }

    schema = load_schema()

    for md_base, md_path in md_by_base.items():
        if md_base not in json_by_base:
            errors.append(
                f"Sin metadata para contenido: {md_path} (esperado {md_base}.json)"
            )

    for json_base, json_path in json_by_base.items():
        if json_base not in md_by_base:
            errors.append(
                f"Metadata sin contenido asociado: {json_path} (esperado {json_base}.md)"
            )

        try:
            with open(json_path, "r", encoding="utf-8") as metadata_file:
                data = json.load(metadata_file)
        except Exception as exc:
            errors.append(f"JSON inválido en {json_path}: {exc}")
            continue

        errors.extend(validate_metadata_types(data, json_path))
        errors.extend(validate_against_schema(data, schema, json_path))

    if errors:
        print("Errores de validación:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Estructura válida")
    return 0


if __name__ == "__main__":
    sys.exit(validate_structure())
