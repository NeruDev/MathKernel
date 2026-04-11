import subprocess
import sys
from pathlib import Path


def test_generate_site_creates_html(tmp_path):
    (tmp_path / "content").mkdir()
    (tmp_path / "metadata").mkdir()
    (tmp_path / "site_src").mkdir()
    (tmp_path / "scripts").mkdir()

    (tmp_path / "content" / "tema.md").write_text("# Tema\n\nContenido.", encoding="utf-8")
    (tmp_path / "metadata" / "tema.json").write_text(
        (
            '{\n'
            '  "id": "tema",\n'
            '  "title": "Tema",\n'
            '  "module": "fundamentos",\n'
            '  "order": 1,\n'
            '  "concepts": ["base"]\n'
            '}\n'
        ),
        encoding="utf-8",
    )
    (tmp_path / "metadata" / "schema.json").write_text(
        (
            '{\n'
            '  "id": "string",\n'
            '  "title": "string",\n'
            '  "module": "string",\n'
            '  "order": "number",\n'
            '  "concepts": ["string"]\n'
            '}\n'
        ),
        encoding="utf-8",
    )

    (tmp_path / "site_src" / "index.html").write_text("<html><body>Inicio</body></html>", encoding="utf-8")
    (tmp_path / "site_src" / "styles.css").write_text("body {}", encoding="utf-8")
    (tmp_path / "site_src" / "scripts.js").write_text("", encoding="utf-8")

    root = Path(__file__).resolve().parents[1]
    for script_name in ("generate_site.py", "validate_structure.py"):
        (tmp_path / "scripts" / script_name).write_text(
            (root / "scripts" / script_name).read_text(encoding="utf-8"),
            encoding="utf-8",
        )

    result = subprocess.run(
        [sys.executable, "scripts/generate_site.py"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + "\n" + result.stderr
    assert (tmp_path / "site" / "pages" / "tema.html").exists()
