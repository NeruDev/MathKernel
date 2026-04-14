# yaml_frontmatter:
#   id: 'validators'
#   script_path: 'scripts/core/validators.py'
#   metadata_path: 'metadata/scripts/core/validators.meta.json'
#   source_of_truth: 'metadata/scripts/**/*.meta.json'
#   title: 'Validadores de espejo y contrato JSON'
#   key_functions:
#     - 'validate_content_mirror'
#     - 'validate_assets_mirror'
#     - 'validate_scripts_mirror'
#     - 'validate_against_schema'
#   tags:
#     - 'validacion'
#     - 'espejo'
#     - 'schema'

from pathlib import Path
from typing import Any

from scripts.core.encoding_validator import validate_utf8_paths


def _to_rel_bases(paths: list[Path], root: Path, suffix: str) -> dict[str, Path]:
    """Mapea rutas absolutas a clave relativa sin sufijo para comparar espejos."""

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
    """Valida correspondencia bidireccional entre dos conjuntos homólogos."""

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
    """Valida espejo 1:1 entre content/*.md y metadata/content/*.json."""

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
    """Valida espejo 1:1 entre assets SVG y metadata de activos."""

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


def validate_scripts_mirror(
    py_files: list[Path],
    json_files: list[Path],
    scripts_root: Path,
    metadata_root: Path,
) -> tuple[list[str], dict[str, Path], dict[str, Path]]:
    """Valida espejo 1:1 entre scripts objetivo y metadata/scripts/*.meta.json."""

    py_rel = _to_rel_bases(py_files, scripts_root, ".py")
    json_rel = _to_rel_bases(json_files, metadata_root, ".meta.json")

    errors = validate_mirror_sets(
        py_rel,
        json_rel,
        left_label="script",
        right_label="metadata de script",
        right_suffix=".meta.json",
        right_root=metadata_root,
    )

    return errors, py_rel, json_rel


def _matches_type(expected_type: str, value: Any) -> bool:
    """Evalua coincidencia de tipo JSON esperado con valor real."""

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


def _validate_schema_node(
    value: Any,
    schema_node: dict[str, Any],
    file_path: Path,
    field_path: str,
) -> list[str]:
    """Valida recursivamente un valor contra un nodo de schema."""

    errors: list[str] = []
    expected_type = schema_node.get("type")

    if isinstance(expected_type, str) and not _matches_type(expected_type, value):
        errors.append(f"Campo '{field_path}' debe ser {expected_type} en {file_path}")
        return errors

    enum_values = schema_node.get("enum")
    if isinstance(enum_values, list) and value not in enum_values:
        errors.append(f"Campo '{field_path}' fuera de enum permitido en {file_path}")

    if expected_type == "array" and isinstance(value, list):
        items_schema = schema_node.get("items")
        if isinstance(items_schema, dict):
            for index, item in enumerate(value):
                errors.extend(
                    _validate_schema_node(
                        item,
                        items_schema,
                        file_path,
                        f"{field_path}[{index}]",
                    )
                )

    if expected_type == "object" and isinstance(value, dict):
        required = schema_node.get("required", [])
        for required_field in required:
            if required_field not in value:
                errors.append(
                    f"Falta campo requerido '{field_path}.{required_field}' en {file_path}"
                )

        properties = schema_node.get("properties", {})
        for child_field, child_value in value.items():
            child_schema = properties.get(child_field)
            if not isinstance(child_schema, dict):
                continue
            errors.extend(
                _validate_schema_node(
                    child_value,
                    child_schema,
                    file_path,
                    f"{field_path}.{child_field}",
                )
            )

    return errors


def validate_against_schema(data: dict[str, Any], schema: dict[str, Any], file_path: Path) -> list[str]:
    """Valida campos requeridos, tipos y enums (incluye estructuras anidadas)."""

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
        errors.extend(_validate_schema_node(value, field_schema, file_path, field))

    return errors


def validate_utf8_targets(targets: list[Path]) -> list[str]:
    """Valida codificacion UTF-8 sobre una lista de rutas objetivo."""

    return validate_utf8_paths(targets)
