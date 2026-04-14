from scripts.core.formula_validator import validate_markdown_math_tables
from utils.markdown import DEFAULT_EXTENSIONS, convert_md_to_html


def test_default_extensions_include_arithmatex():
    assert "pymdownx.arithmatex" in DEFAULT_EXTENSIONS


def test_detects_unbalanced_math_delimiters():
    md_text = "Formula incompleta: $a + b"
    warnings = validate_markdown_math_tables(md_text, "demo.md")

    assert any("desbalanceados" in warning for warning in warnings)


def test_detects_table_without_blank_line_before():
    md_text = "**Entre rectas:**\n| A | B |\n|---|---|\n| x | y |"
    warnings = validate_markdown_math_tables(md_text, "demo.md")

    assert any("sin linea en blanco previa" in warning for warning in warnings)


def test_arithmatex_renders_formula_inside_table():
    md_text = "| Propiedad | Formula |\n|---|---|\n| Conmutativa | $a+b=b+a$ |"
    html, _ = convert_md_to_html(md_text)

    assert "<table>" in html
    assert "arithmatex" in html