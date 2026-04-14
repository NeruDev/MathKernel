import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT_ROLE_BY_NAME = {
    "build": "orchestrator",
    "config": "config",
    "generate_assets": "generator",
    "migrate_content_yaml_frontmatter": "migration",
    "templates": "template",
    "validate_encoding": "validator",
    "validate_markdown_format": "validator",
    "validators": "validator",
    "processors": "processor",
    "generators": "generator",
    "formula_validator": "validator",
    "error_handling": "error_model",
    "encoding_validator": "validator",
    "file_manager": "io_manager",
}


def _is_target_script(script_path: Path, scripts_root: Path) -> bool:
    if script_path.suffix != ".py" or script_path.name == "__init__.py":
        return False

    rel_path = script_path.relative_to(scripts_root)
    if len(rel_path.parts) == 1:
        return True
    return rel_path.parts[0] in {"core", "io"}


def _script_metadata_payload(rel_path: Path) -> dict:
    stem = rel_path.stem
    script_rel = Path("scripts") / rel_path
    metadata_rel = Path("metadata") / "scripts" / rel_path.with_suffix(".meta.json")
    role = SCRIPT_ROLE_BY_NAME.get(stem, "validator")

    return {
        "file_name": rel_path.name,
        "script_path": script_rel.as_posix(),
        "metadata_path": metadata_rel.as_posix(),
        "description": f"Metadata de prueba para {rel_path.as_posix()}.",
        "repo_role": role,
        "inputs": ["entrada_prueba"],
        "outputs": ["salida_prueba"],
        "dependencies": {
            "external": [],
            "internal": [],
        },
        "tags": ["test", stem],
        "key_functions": [],
        "usage_example": f"python {script_rel.as_posix()}",
        "performance_constraints": "Sin restricciones especificas en fixture de pruebas.",
        "known_limitations": "Documento sintetico para sandbox de pruebas.",
        "status": "production",
        "maintainer": "tests",
    }


@pytest.fixture
def repo_root():
    return Path(__file__).resolve().parents[1]


@pytest.fixture
def sandbox_project(tmp_path, repo_root):
    (tmp_path / "content").mkdir()
    (tmp_path / "metadata" / "content").mkdir(parents=True)
    (tmp_path / "metadata" / "assets" / "images" / "grafics" / "00_fundamentos" / "tema").mkdir(parents=True)
    (tmp_path / "metadata" / "schemas").mkdir(parents=True)
    (tmp_path / "metadata" / "scripts").mkdir(parents=True)
    (tmp_path / "site_src").mkdir()
    (tmp_path / "assets" / "images" / "grafics" / "00_fundamentos" / "tema").mkdir(parents=True)

    (tmp_path / "content" / "tema.md").write_text(
        "# Tema\n\n## 1.1 Seccion\n\n[Ver tema](tema.md)\n\nContenido.",
        encoding="utf-8",
    )

    metadata_content = {
        "id": "tema",
        "title": "Tema",
        "module": "00_fundamentos",
        "order": 1,
        "concepts": ["base"],
        "scripts": ["circulo.py"],
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
        "required": ["id", "image_path", "description", "section"],
        "properties": {
            "id": {"type": "string"},
            "image_path": {"type": "string"},
            "description": {"type": "string"},
            "section": {"type": "string"},
        },
    }
    (tmp_path / "metadata" / "schemas" / "assets.schema.json").write_text(
        json.dumps(assets_schema, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    scripts_schema = {
        "required": [
            "file_name",
            "script_path",
            "metadata_path",
            "description",
            "repo_role",
            "inputs",
            "outputs",
            "dependencies",
            "tags",
            "key_functions",
            "usage_example",
            "performance_constraints",
            "known_limitations",
            "status",
            "maintainer",
        ],
        "properties": {
            "file_name": {"type": "string"},
            "script_path": {"type": "string"},
            "metadata_path": {"type": "string"},
            "description": {"type": "string"},
            "repo_role": {
                "type": "string",
                "enum": [
                    "orchestrator",
                    "config",
                    "generator",
                    "migration",
                    "template",
                    "validator",
                    "processor",
                    "error_model",
                    "io_manager",
                ],
            },
            "inputs": {"type": "array", "items": {"type": "string"}},
            "outputs": {"type": "array", "items": {"type": "string"}},
            "dependencies": {
                "type": "object",
                "required": ["external", "internal"],
                "properties": {
                    "external": {"type": "array", "items": {"type": "string"}},
                    "internal": {"type": "array", "items": {"type": "string"}},
                },
            },
            "tags": {"type": "array", "items": {"type": "string"}},
            "key_functions": {"type": "array", "items": {"type": "string"}},
            "usage_example": {"type": "string"},
            "performance_constraints": {"type": "string"},
            "known_limitations": {"type": "string"},
            "status": {
                "type": "string",
                "enum": ["draft", "testing", "production", "deprecated"],
            },
            "maintainer": {"type": "string"},
        },
    }
    (tmp_path / "metadata" / "schemas" / "scripts.schema.json").write_text(
        json.dumps(scripts_schema, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    asset_metadata = {
        "id": "circulo",
        "category": "00_fundamentos",
        "topic": "tema",
        "topic_id": "FUN-00",
        "script_source": "scripts/grafics/00_fundamentos/tema/circulo.py",
        "image_path": "assets/images/grafics/00_fundamentos/tema/circulo.svg",
        "description": "Circulo unitario",
        "used_in": [],
        "section": "1.1 Seccion",
        "format": "SVG",
    }
    (tmp_path / "metadata" / "assets" / "images" / "grafics" / "00_fundamentos" / "tema" / "circulo.json").write_text(
        json.dumps(asset_metadata, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    (tmp_path / "assets" / "images" / "grafics" / "00_fundamentos" / "tema" / "circulo.svg").write_text(
        "<svg xmlns='http://www.w3.org/2000/svg'></svg>",
        encoding="utf-8",
    )

    for site_file in ("index.html", "styles.css", "scripts.js", "template_page.html"):
        shutil.copy2(repo_root / "site_src" / site_file, tmp_path / "site_src" / site_file)

    shutil.copytree(
        repo_root / "scripts",
        tmp_path / "scripts",
        ignore=shutil.ignore_patterns("grafics", "__pycache__"),
    )

    shutil.copytree(repo_root / "utils", tmp_path / "utils")

    scripts_root = tmp_path / "scripts"
    metadata_scripts_root = tmp_path / "metadata" / "scripts"
    for script_path in sorted(scripts_root.rglob("*.py")):
        if not _is_target_script(script_path, scripts_root):
            continue

        rel_script_path = script_path.relative_to(scripts_root)
        metadata_path = metadata_scripts_root / rel_script_path.with_suffix(".meta.json")
        metadata_path.parent.mkdir(parents=True, exist_ok=True)
        metadata_path.write_text(
            json.dumps(_script_metadata_payload(rel_script_path), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    return tmp_path


@pytest.fixture
def run_script():
    def _run(project_dir, script_rel_path, *args):
        return subprocess.run(
            [sys.executable, script_rel_path, *args],
            cwd=project_dir,
            capture_output=True,
            text=True,
            check=False,
        )

    return _run
