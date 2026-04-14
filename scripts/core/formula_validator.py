# yaml_frontmatter:
#   id: 'formula_validator'
#   script_path: 'scripts/core/formula_validator.py'
#   metadata_path: 'metadata/scripts/core/formula_validator.meta.json'
#   source_of_truth: 'metadata/scripts/**/*.meta.json'
#   title: 'Validador de delimitadores matematicos y tablas markdown'
#   key_functions:
#     - 'validate_markdown_math_tables'
#   tags:
#     - 'validacion'
#     - 'markdown'
#     - 'matematicas'

import re
from pathlib import Path

TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|(?:\s*:?-{3,}:?\s*\|)+\s*$")


def _scan_unbalanced_math_delimiters(md_text: str) -> bool:
    """Detecta delimitadores $ y $$ desbalanceados respetando escapes."""

    in_inline = False
    in_block = False
    i = 0

    while i < len(md_text):
        current = md_text[i]
        escaped = i > 0 and md_text[i - 1] == "\\"

        if current == "$" and not escaped:
            next_is_dollar = i + 1 < len(md_text) and md_text[i + 1] == "$"
            if next_is_dollar:
                in_block = not in_block
                i += 2
                continue
            if not in_block:
                in_inline = not in_inline
        i += 1

    return in_inline or in_block


def _validate_table_block(lines: list[str], start_index: int, source: str) -> list[str]:
    """Valida separador y consistencia de columnas en un bloque de tabla."""

    warnings: list[str] = []

    if len(lines) < 2:
        warnings.append(
            f"[WARN] Tabla incompleta en {source}:{start_index + 1} (falta separador y filas)."
        )
        return warnings

    if not TABLE_SEPARATOR_RE.match(lines[1]):
        warnings.append(
            f"[WARN] Tabla sin separador valido en {source}:{start_index + 2}."
        )
        return warnings

    expected_pipes = lines[0].count("|")
    for offset, row in enumerate(lines[2:], start=3):
        if row.count("|") != expected_pipes:
            warnings.append(
                f"[WARN] Tabla con columnas inconsistentes en {source}:{start_index + offset}."
            )

    return warnings


def validate_markdown_math_tables(md_text: str, source_path: Path | str) -> list[str]:
    """Aplica validaciones de formulas/tablas y retorna advertencias no bloqueantes."""

    source = str(source_path)
    warnings: list[str] = []

    if _scan_unbalanced_math_delimiters(md_text):
        warnings.append(
            f"[WARN] Delimitadores matematicos desbalanceados en {source}."
        )

    lines = md_text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not TABLE_ROW_RE.match(line):
            index += 1
            continue

        start = index
        block: list[str] = []
        while index < len(lines) and TABLE_ROW_RE.match(lines[index]):
            block.append(lines[index])
            index += 1

        if start > 0 and lines[start - 1].strip() and not TABLE_ROW_RE.match(lines[start - 1]):
            warnings.append(
                f"[WARN] Tabla sin linea en blanco previa en {source}:{start + 1}."
            )

        warnings.extend(_validate_table_block(block, start, source))

    return warnings