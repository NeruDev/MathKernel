from utils.metadata import extract_metadata_fields, validate_required_fields


def test_extract_metadata_fields_defaults():
    fields = extract_metadata_fields({"id": "x"})

    assert fields["id"] == "x"
    assert fields["title"] is None
    assert fields["module"] is None
    assert fields["order"] is None
    assert fields["concepts"] == []


def test_validate_required_fields_missing():
    missing = validate_required_fields({"id": "x"}, ["id", "title", "module"])
    assert missing == ["title", "module"]


def test_glossary_and_index_generation_from_metadata(sandbox_project, run_script):
    result = run_script(sandbox_project, "scripts/build.py")
    assert result.returncode == 0

    glossary_html = (sandbox_project / "site" / "glossary.html").read_text(encoding="utf-8")
    index_html = (sandbox_project / "site" / "index.html").read_text(encoding="utf-8")

    assert "base" in glossary_html
    assert "Tema" in index_html
