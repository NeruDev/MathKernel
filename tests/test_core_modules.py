from pathlib import Path

from scripts.core import generators, processors, validators


def test_validators_detect_missing_metadata(tmp_path):
    content_root = tmp_path / "content"
    metadata_root = tmp_path / "metadata"
    content_root.mkdir(parents=True)
    metadata_root.mkdir(parents=True)

    md_file = content_root / "tema.md"
    md_file.write_text("# Tema", encoding="utf-8")

    errors, _, _ = validators.validate_content_mirror([md_file], [], content_root, metadata_root)

    assert errors
    assert "Sin metadata" in errors[0]


def test_processors_inject_image_in_section():
    source = "# Tema\n\n## 1.1 Seccion\n\nTexto.\n"
    image_md = "![img](assets/images/a.svg)"

    updated, inserted, reason = processors.inject_image_markdown(source, image_md, "1.1 Seccion")

    assert inserted is True
    assert reason == "section"
    assert image_md in updated


def test_generators_build_index_items_and_body():
    records = [
        {
            "id": "tema",
            "title": "Tema",
            "module": "00_fundamentos",
            "order": 1,
            "concepts": ["base"],
        }
    ]
    id_to_path = {"tema": "tema.html"}

    items, warnings = generators.build_index_items(records, id_to_path)

    assert not warnings
    assert items[0]["title"] == "Tema"
    body = generators.build_index_body(items)
    assert "Biblioteca Matemática" in body
    assert "tema.html" in body
