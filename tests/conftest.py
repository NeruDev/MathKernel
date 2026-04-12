import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture
def repo_root():
    return Path(__file__).resolve().parents[1]


@pytest.fixture
def sandbox_project(tmp_path, repo_root):
    (tmp_path / "content").mkdir()
    (tmp_path / "metadata" / "content").mkdir(parents=True)
    (tmp_path / "metadata" / "assets" / "images" / "grafics").mkdir(parents=True)
    (tmp_path / "metadata" / "schemas").mkdir(parents=True)
    (tmp_path / "site_src").mkdir()
    (tmp_path / "scripts").mkdir()

    (tmp_path / "content" / "tema.md").write_text(
        "# Tema\n\n[Ver tema](tema.md)\n\nContenido.",
        encoding="utf-8",
    )

    metadata_content = {
        "id": "tema",
        "title": "Tema",
        "module": "00_fundamentos",
        "order": 1,
        "concepts": ["base"],
    }
    (tmp_path / "metadata" / "content" / "tema.json").write_text(
        json.dumps(metadata_content, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    content_schema = {
        "required": ["id", "title", "module", "order", "concepts"],
        "properties": {
            "id": {"type": "string"},
            "title": {"type": "string"},
            "module": {"type": "string"},
            "order": {"type": "integer"},
            "concepts": {"type": "array"},
        },
    }
    (tmp_path / "metadata" / "schemas" / "content.schema.json").write_text(
        json.dumps(content_schema, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    assets_schema = {
        "required": ["id", "image_path"],
        "properties": {
            "id": {"type": "string"},
            "image_path": {"type": "string"},
        },
    }
    (tmp_path / "metadata" / "schemas" / "assets.schema.json").write_text(
        json.dumps(assets_schema, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    for site_file in ("index.html", "styles.css", "scripts.js", "template_page.html"):
        shutil.copy2(repo_root / "site_src" / site_file, tmp_path / "site_src" / site_file)

    for script_file in ("generate_site.py", "validate_structure.py"):
        shutil.copy2(repo_root / "scripts" / script_file, tmp_path / "scripts" / script_file)

    shutil.copytree(repo_root / "utils", tmp_path / "utils")

    return tmp_path


@pytest.fixture
def run_script():
    def _run(project_dir, script_rel_path):
        return subprocess.run(
            [sys.executable, script_rel_path],
            cwd=project_dir,
            capture_output=True,
            text=True,
            check=False,
        )

    return _run
