# yaml_frontmatter:
#   id: 'generators'
#   script_path: 'scripts/core/generators.py'
#   metadata_path: 'metadata/scripts/core/generators.meta.json'
#   source_of_truth: 'metadata/scripts/**/*.meta.json'
#   title: 'Generadores de cuerpo HTML para indice y glosario'
#   key_functions:
#     - 'build_glossary_body'
#     - 'build_index_items'
#     - 'build_index_body'
#   tags:
#     - 'generacion'
#     - 'html'
#     - 'metadata'

import re
from pathlib import Path
from typing import Any

from utils.metadata import extract_metadata_fields, validate_required_fields
from utils.pathing import build_relative_prefix


def format_display_title(file_stem: str) -> str:
    """Formatea un stem en titulo legible para interfaz web."""

    return file_stem.replace("_", " ").title()


def wrap_html(title: str, body: str, template_html: str, depth: int) -> str:
    """Envuelve contenido HTML en template aplicando prefijo relativo de assets."""

    prefix = build_relative_prefix(depth)
    return (
        template_html.replace("{{TITLE}}", title)
        .replace("{{BODY}}", body)
        .replace("{{PREFIX}}", prefix)
    )


def build_glossary_body(metadata_records: list[dict[str, Any]]) -> str:
    """Genera HTML del glosario agregando conceptos unicos de metadata."""

    concepts: list[str] = []
    for data in metadata_records:
        fields = extract_metadata_fields(data)
        concepts.extend(fields["concepts"])

    unique_concepts: list[str] = []
    seen: set[str] = set()
    for concept in concepts:
        if concept in seen:
            continue
        seen.add(concept)
        unique_concepts.append(concept)

    list_items = "".join(f"<li>{item}</li>" for item in unique_concepts)
    return f"<h1>Glosario de Conceptos</h1><ul>{list_items}</ul>"


def build_index_items(
    metadata_records: list[dict[str, Any]],
    id_to_path: dict[str, str],
) -> tuple[list[dict[str, Any]], list[str]]:
    """Construye items de indice ordenados y sus advertencias de integridad."""

    items: list[dict[str, Any]] = []
    warnings: list[str] = []

    for data in metadata_records:
        missing = validate_required_fields(data, ["id"])
        if missing:
            warnings.append(f"Metadata invalida: faltan campos {missing}")
            continue

        md_id = data["id"]
        if md_id not in id_to_path:
            warnings.append(f"ID {md_id} de metadata no encontrado en contenido")
            continue

        fields = extract_metadata_fields(data)
        items.append(
            {
                "title": fields["title"] or md_id,
                "module": fields["module"] or "zz_sin_modulo",
                "order": fields["order"] if isinstance(fields["order"], int) else 9999,
                "link": f"./{id_to_path[md_id]}",
            }
        )

    items.sort(key=lambda item: (item["module"], item["order"]))
    return items, warnings


def build_index_body(items: list[dict[str, Any]]) -> str:
    """Renderiza bloques HTML del indice agrupados por modulo."""

    current_module: str | None = None
    chunks: list[str] = [
        "<h1>Biblioteca Matemática</h1>",
        "<p>Índice completo de temas disponibles en MathKernel.</p>",
    ]

    for item in items:
        module = item["module"]
        if module != current_module:
            if current_module is not None:
                chunks.append("</ul>")
            current_module = module
            clean_module = re.sub(r"^\d+_", "", module).replace("_", " ").title()
            chunks.append(f"<h3>{clean_module}</h3><ul>")

        chunks.append(f'<li><a href="{item["link"]}">{item["title"]}</a></li>')

    if current_module is not None:
        chunks.append("</ul>")

    return "".join(chunks)


def metadata_json_paths(metadata_content_dir: Path) -> list[Path]:
    """Lista metadatos JSON de contenido ignorando schema.json heredado."""

    return [
        path
        for path in sorted(metadata_content_dir.rglob("*.json"))
        if path.name != "schema.json"
    ]
