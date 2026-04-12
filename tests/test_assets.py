import json
from pathlib import Path

def test_link_assets_to_content(sandbox_project, run_script):
    # Setup: Create a file that matches TOPIC_TO_FILE mapping in link_assets_to_content.py
    # FUN-04 -> 00_fundamentos/04_geometria/geometria.md
    md_dir = sandbox_project / "content" / "00_fundamentos" / "04_geometria"
    md_dir.mkdir(parents=True)
    md_file = md_dir / "geometria.md"
    md_file.write_text("## 4.2 Ángulos\n\nTexto original.", encoding="utf-8")

    # Create asset metadata
    asset_metadata_dir = sandbox_project / "metadata" / "assets" / "images" / "grafics" / "00_fundamentos" / "04_geometria"
    asset_metadata_dir.mkdir(parents=True)
    asset_json = asset_metadata_dir / "circulo.json"
    asset_data = {
        "id": "circulo",
        "topic_id": "FUN-04",
        "section": "4.2 Ángulos",
        "description": "Un círculo unitario",
        "image_path": "assets/images/grafics/00_fundamentos/04_geometria/circulo.svg"
    }
    asset_json.write_text(json.dumps(asset_data), encoding="utf-8")

    # Run the script
    result = run_script(sandbox_project, "scripts/link_assets_to_content.py")
    assert result.returncode == 0

    # Verify content
    updated_content = md_file.read_text(encoding="utf-8")
    assert "![Un círculo unitario](../../../assets/images/grafics/00_fundamentos/04_geometria/circulo.svg)" in updated_content
    assert "## 4.2 Ángulos" in updated_content

def test_link_assets_no_duplicates(sandbox_project, run_script):
    md_dir = sandbox_project / "content" / "00_fundamentos" / "04_geometria"
    md_dir.mkdir(parents=True, exist_ok=True)
    md_file = md_dir / "geometria.md"
    img_link = "![Un círculo unitario](../../../assets/images/grafics/00_fundamentos/04_geometria/circulo.svg)"
    md_file.write_text(f"## 4.2 Ángulos\n\n{img_link}\n\nTexto.", encoding="utf-8")

    asset_metadata_dir = sandbox_project / "metadata" / "assets" / "images" / "grafics" / "00_fundamentos" / "04_geometria"
    asset_metadata_dir.mkdir(parents=True, exist_ok=True)
    asset_json = asset_metadata_dir / "circulo.json"
    asset_data = {
        "id": "circulo",
        "topic_id": "FUN-04",
        "section": "4.2 Ángulos",
        "description": "Un círculo unitario",
        "image_path": "assets/images/grafics/00_fundamentos/04_geometria/circulo.svg"
    }
    asset_json.write_text(json.dumps(asset_data), encoding="utf-8")

    # Run twice
    run_script(sandbox_project, "scripts/link_assets_to_content.py")
    result = run_script(sandbox_project, "scripts/link_assets_to_content.py")
    
    assert result.returncode == 0
    content = md_file.read_text(encoding="utf-8")
    # Should only appear once
    assert content.count(img_link) == 1
