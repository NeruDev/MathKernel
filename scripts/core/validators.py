from pathlib import Path
from typing import Any

from scripts.core.encoding_validator import validate_utf8_paths


def _to_rel_bases(paths: list[Path], root: Path, suffix: str) -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    for path in paths:
        rel = path.relative_to(root).as_posix()
        if rel.endswith(suffix):
            rel = rel[: -len(suffix)]
        mapping[rel] = path
    return mapping


def validate_mirror_sets(
    left_rel: dict[str, Path],
    right_rel: dict[str, Path],
    *,
    left_label: str,
    right_label: str,
    right_suffix: str,
    right_root: Path,
) -> list[str]:
    errors: list[str] = []

    for rel_base, left_path in left_rel.items():
        if rel_base not in right_rel:
            expected = right_root / f"{rel_base}{right_suffix}"
            errors.append(
                f"[ERROR] Sin {right_label} para {left_label}: {left_path} (esperado {expected})"
            )

    for rel_base, right_path in right_rel.items():
        if rel_base not in left_rel:
            errors.append(
                f"[ERROR] {right_label} sin {left_label}: {right_path}"
            )

    return errors


def validate_content_mirror(
    md_files: list[Path],
    json_files: list[Path],
    content_root: Path,
    metadata_root: Path,
) -> tuple[list[str], dict[str, Path], dict[str, Path]]:
    md_rel = _to_rel_bases(md_files, content_root, ".md")
    json_rel = _to_rel_bases(json_files, metadata_root, ".json")

    errors = validate_mirror_sets(
        md_rel,
        json_rel,
        left_label="contenido",
        right_label="metadata",
        right_suffix=".json",
        right_root=metadata_root,
    )

    return errors, md_rel, json_rel


def validate_assets_mirror(
    svg_files: list[Path],
    json_files: list[Path],
    assets_root: Path,
    metadata_root: Path,
) -> tuple[list[str], dict[str, Path], dict[str, Path]]:
    svg_rel = _to_rel_bases(svg_files, assets_root, ".svg")
    json_rel = _to_rel_bases(json_files, metadata_root, ".json")

    errors = validate_mirror_sets(
        svg_rel,
        json_rel,
        left_label="imagen",
        right_label="metadata de activo",
        right_suffix=".json",
        right_root=metadata_root,
    )

    return errors, svg_rel, json_rel


def _matches_type(expected_type: str, value: Any) -> bool:
    if expected_type == "string":
        return isinstance(value, str)
    if expected_type == "array":
        return isinstance(value, list)
    if expected_type == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected_type == "boolean":
        return isinstance(value, bool)
    if expected_type == "object":
        return isinstance(value, dict)
    return True


def validate_against_schema(data: dict[str, Any], schema: dict[str, Any], file_path: Path) -> list[str]:
    errors: list[str] = []
    if not schema:
        return errors

    required = schema.get("required", [])
    for field in required:
        if field not in data:
            errors.append(f"Falta campo requerido '{field}' en {file_path}")

    properties = schema.get("properties", {})
    for field, value in data.items():
        field_schema = properties.get(field)
        if not isinstance(field_schema, dict):
            continue

        expected_type = field_schema.get("type")
        if isinstance(expected_type, str) and not _matches_type(expected_type, value):
            errors.append(
                f"Campo '{field}' debe ser {expected_type} en {file_path}"
            )

    return errors


def validate_utf8_targets(targets: list[Path]) -> list[str]:
    return validate_utf8_paths(targets)
