# yaml_frontmatter:
#   id: 'validate_markdown_format'
#   script_path: 'scripts/validate_markdown_format.py'
#   metadata_path: 'metadata/scripts/validate_markdown_format.meta.json'
#   source_of_truth: 'metadata/scripts/**/*.meta.json'
#   title: 'Validador informativo de formulas y tablas markdown'
#   key_functions:
#     - '_parse_args'
#     - 'main'
#   tags:
#     - 'validacion'
#     - 'markdown'
#     - 'formulas'

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.config import Paths
from scripts.core.formula_validator import validate_markdown_math_tables
from scripts.io.file_manager import FileManager
from utils.logging import log_info, log_warn
from utils.markdown import convert_md_to_html

RAW_MATH_HTML_RE = re.compile(r">\s*\$[^<\n]+\$\s*<")
RAW_TABLE_HTML_RE = re.compile(r"^\s*\|.*\|\s*$", re.MULTILINE)


def _parse_args() -> argparse.Namespace:
    """Parsea opciones de ejecucion del validador markdown."""

    parser = argparse.ArgumentParser(
        description="Valida formulas y tablas Markdown en modo informativo"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Retorna codigo 1 si se detectan alertas",
    )
    return parser.parse_args()


def main() -> int:
    """Valida markdown de content/ y reporta alertas informativas o estrictas."""

    args = _parse_args()
    paths = Paths.from_project_root(PROJECT_ROOT)
    manager = FileManager()

    warnings: list[str] = []
    for md_path in sorted(paths.content_dir.rglob("*.md")):
        md_text = manager.read_text(md_path)
        warnings.extend(validate_markdown_math_tables(md_text, md_path))

        html, _ = convert_md_to_html(md_text)
        if RAW_TABLE_HTML_RE.search(html):
            warnings.append(
                f"[WARN] Tabla no renderizada correctamente en {md_path} (render HTML contiene filas crudas)."
            )
        if RAW_MATH_HTML_RE.search(html):
            warnings.append(
                f"[WARN] Formula sin encapsular por arithmatex en {md_path}."
            )

    if warnings:
        for warning in warnings:
            log_warn(warning)
        log_info(f"Validacion Markdown finalizada con {len(warnings)} alertas informativas")
        return 1 if args.strict else 0

    log_info("Validacion Markdown finalizada sin alertas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())