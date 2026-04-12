import subprocess
import sys
import os
from pathlib import Path

def test_generate_site_creates_html(tmp_path):
    # Crear estructura homóloga
    (tmp_path / "content").mkdir()
    (tmp_path / "metadata").mkdir()
    (tmp_path / "metadata" / "content").mkdir()
    (tmp_path / "metadata" / "schemas").mkdir()
    (tmp_path / "site_src").mkdir()
    (tmp_path / "scripts").mkdir()

    # Crear archivos de prueba siguiendo la nueva arquitectura
    (tmp_path / "content" / "tema.md").write_text("# Tema\n\nContenido.", encoding="utf-8")
    
    # Metadato en la carpeta espejo metadata/content/
    (tmp_path / "metadata" / "content" / "tema.json").write_text(
        json_data := (
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
    
    # Esquema en la carpeta centralizada metadata/schemas/
    (tmp_path / "metadata" / "schemas" / "content.schema.json").write_text(
        '{"required": ["id", "title", "module", "order", "concepts"]}',
        encoding="utf-8",
    )

    (tmp_path / "site_src" / "index.html").write_text("<html><body>Inicio</body></html>", encoding="utf-8")
    (tmp_path / "site_src" / "styles.css").write_text("body {}", encoding="utf-8")
    (tmp_path / "site_src" / "scripts.js").write_text("", encoding="utf-8")

    # Copiar los scripts reales al entorno temporal
    root = Path(__file__).resolve().parents[1]
    for script_name in ("generate_site.py", "validate_structure.py"):
        (tmp_path / "scripts" / script_name).write_text(
            (root / "scripts" / script_name).read_text(encoding="utf-8"),
            encoding="utf-8",
        )

    # Ejecutar el build
    result = subprocess.run(
        [sys.executable, "scripts/generate_site.py"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )

    # Verificaciones
    assert result.returncode == 0, f"Error en build:\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
    assert (tmp_path / "site" / "pages" / "tema.html").exists()
    assert (tmp_path / "site" / "index.html").exists()
    assert (tmp_path / "site" / "glossary.html").exists()
