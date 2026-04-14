# yaml_frontmatter:
#   id: 'migrate_content_yaml_frontmatter'
#   script_path: 'scripts/migrate_content_yaml_frontmatter.py'
#   metadata_path: 'metadata/scripts/migrate_content_yaml_frontmatter.meta.json'
#   source_of_truth: 'metadata/scripts/**/*.meta.json'
#   title: 'Migrador de frontmatter YAML comentado y glosario para content'
#   key_functions:
#     - '_build_frontmatter_comment'
#     - '_update_markdown_file'
#     - 'main'
#   tags:
#     - 'migracion'
#     - 'yaml_frontmatter'
#     - 'markdown'

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.config import Paths
from scripts.core.error_handling import FileOperationError
from scripts.io.file_manager import FileManager
from utils.logging import log_error, log_info, log_warn

FRONTMATTER_BLOCK_RE = re.compile(
    r"^\s*<!--\s*yaml_frontmatter:\s*.*?-->\s*",
    re.DOTALL,
)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
FORMULA_RE = re.compile(r"\$[^$\n]{1,400}\$|\$\$.+?\$\$", re.DOTALL)
EQUATION_RE = re.compile(r"\b[A-Za-z]\s*=\s*[^=\n]+")
GLOSSARY_SECTION_RE = re.compile(r"^##\s+Glosario de variables\b", re.IGNORECASE | re.MULTILINE)
PI_RE = re.compile(r"\\pi|π|\bpi\b", re.IGNORECASE)
EULER_RE = re.compile(r"Euler|\\mathrm\{e\}|e\^", re.IGNORECASE)

VARIABLE_CANDIDATES = ["x", "y", "z", "t", "n", "m", "k", "r", "u", "v", "w"]


def _yaml_quote(value: str) -> str:
    """Escapa comillas simples para serializar valores seguros en YAML."""

    escaped = value.replace("'", "''")
    return f"'{escaped}'"


def _strip_frontmatter_block(md_text: str) -> str:
    """Elimina el bloque yaml_frontmatter comentado si ya existe."""

    return FRONTMATTER_BLOCK_RE.sub("", md_text, count=1).lstrip("\n")


def _extract_headings(md_text: str, max_items: int = 8) -> list[str]:
    """Extrae encabezados markdown unicos para resumir estructura del tema."""

    headings: list[str] = []
    for line in md_text.splitlines():
        match = HEADING_RE.match(line.strip())
        if not match:
            continue

        heading = match.group(1).strip()
        if heading and heading not in headings:
            headings.append(heading)
        if len(headings) >= max_items:
            break

    return headings


def _extract_variable_symbols(md_text: str, max_items: int = 6) -> list[str]:
    """Detecta simbolos de variables frecuentes dentro de formulas del tema."""

    symbols: list[str] = []

    formula_chunks = FORMULA_RE.findall(md_text)
    formula_text = "\n".join(formula_chunks)

    for symbol in VARIABLE_CANDIDATES:
        pattern = re.compile(rf"(?<![A-Za-z]){re.escape(symbol)}(?![A-Za-z])")
        if pattern.search(formula_text):
            symbols.append(symbol)
        if len(symbols) >= max_items:
            break

    return symbols


def _needs_glossary(md_text: str) -> bool:
    """Determina si el contenido requiere seccion de glosario de variables."""

    return bool(FORMULA_RE.search(md_text) or EQUATION_RE.search(md_text))


def _build_glossary_section(md_text: str) -> str:
    """Construye una tabla markdown de variables y constantes detectadas."""

    rows: list[tuple[str, str, str, str, str, str]] = []

    if PI_RE.search(md_text):
        rows.append(("π", "Constante pi", "constante", "rad", "3.14159265359", "12"))
    if EULER_RE.search(md_text):
        rows.append(("e", "Numero de Euler", "constante", "N/A", "2.71828182846", "12"))

    for symbol in _extract_variable_symbols(md_text):
        rows.append((symbol, f"Variable {symbol}", "variable", "N/A", "N/A", "N/A"))

    if not rows:
        rows.append(("N/A", "Completar segun tema", "variable", "N/A", "N/A", "N/A"))

    lines = [
        "## Glosario de variables",
        "",
        "| Simbolo | Nombre | Tipo | Unidad | Valor | Precision |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for symbol, name, kind, unit, value, precision in rows:
        lines.append(f"| {symbol} | {name} | {kind} | {unit} | {value} | {precision} |")

    return "\n".join(lines) + "\n"


def _build_frontmatter_comment(
    md_rel_path: str,
    metadata_rel_path: str,
    file_id: str,
    title: str,
    headings: list[str],
    concepts: list[str],
) -> str:
    """Construye el bloque YAML comentado que sirve de referencia para IA."""

    lines = [
        "<!--",
        "yaml_frontmatter:",
        f"  id: {_yaml_quote(file_id)}",
        f"  content_path: {_yaml_quote(md_rel_path)}",
        f"  metadata_path: {_yaml_quote(metadata_rel_path)}",
        "  source_of_truth: 'metadata/content/*.json'",
        f"  title: {_yaml_quote(title)}",
        "  key_headings:",
    ]

    if headings:
        for heading in headings:
            lines.append(f"    - {_yaml_quote(heading)}")
    else:
        lines.append("    - 'N/A'")

    lines.append("  key_concepts:")
    if concepts:
        for concept in concepts[:10]:
            lines.append(f"    - {_yaml_quote(str(concept))}")
    else:
        lines.append("    - 'N/A'")

    lines.append("-->")
    lines.append("")
    return "\n".join(lines)


def _update_markdown_file(paths: Paths, file_manager: FileManager, md_path: Path, dry_run: bool) -> tuple[bool, bool]:
    """Actualiza un archivo markdown con frontmatter comentado y glosario opcional."""

    md_rel_path = md_path.relative_to(paths.project_root).as_posix()
    rel_to_content = md_path.relative_to(paths.content_dir).with_suffix(".json")
    metadata_path = paths.metadata_content_dir / rel_to_content
    metadata_rel_path = metadata_path.relative_to(paths.project_root).as_posix()

    raw_content = file_manager.read_text(md_path)
    body_content = _strip_frontmatter_block(raw_content)

    metadata: dict = {}
    if metadata_path.exists():
        metadata = file_manager.read_json(metadata_path)
    else:
        log_warn(f"Metadata faltante para {md_rel_path}: {metadata_rel_path}")

    headings = _extract_headings(body_content)
    title = str(metadata.get("title") or (headings[0] if headings else md_path.stem.replace("_", " ").title()))
    concepts = metadata.get("concepts", []) if isinstance(metadata.get("concepts", []), list) else []

    frontmatter_comment = _build_frontmatter_comment(
        md_rel_path=md_rel_path,
        metadata_rel_path=metadata_rel_path,
        file_id=str(metadata.get("id") or md_path.stem),
        title=title,
        headings=headings,
        concepts=concepts,
    )

    new_content = frontmatter_comment + body_content
    glossary_added = False

    if _needs_glossary(body_content) and not GLOSSARY_SECTION_RE.search(body_content):
        if not new_content.endswith("\n"):
            new_content += "\n"
        new_content += "\n" + _build_glossary_section(body_content)
        glossary_added = True

    changed = new_content != raw_content
    if changed and not dry_run:
        file_manager.write_text(md_path, new_content)

    return changed, glossary_added


def parse_args() -> argparse.Namespace:
    """Parsea argumentos del migrador de frontmatter."""

    parser = argparse.ArgumentParser(description="Inserta YAML comentado y glosario en content/*.md")
    parser.add_argument("--dry-run", action="store_true", help="Analiza sin escribir cambios")
    return parser.parse_args()


def main() -> int:
    """Ejecuta la migracion sobre content/*.md y reporta resumen final."""

    args = parse_args()
    file_manager = FileManager()
    paths = Paths.from_project_root(PROJECT_ROOT)

    if not paths.content_dir.exists():
        log_error(f"No existe carpeta content/: {paths.content_dir}")
        return 1

    md_files = sorted(paths.content_dir.rglob("*.md"))
    updated_count = 0
    glossary_count = 0

    for md_path in md_files:
        try:
            changed, glossary_added = _update_markdown_file(paths, file_manager, md_path, args.dry_run)
        except FileOperationError as exc:
            log_error(f"Error en {md_path}: {exc}")
            return 1

        if changed:
            updated_count += 1
            if glossary_added:
                glossary_count += 1
            log_info(f"Actualizado: {md_path.relative_to(paths.project_root).as_posix()}")

    mode = "(dry-run) " if args.dry_run else ""
    log_info(
        f"{mode}Migracion completada: {updated_count} archivos con frontmatter YAML comentado, "
        f"{glossary_count} glosarios insertados"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
