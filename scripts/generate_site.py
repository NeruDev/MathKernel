import os
import re
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.io import copy_dir, ensure_dir, read_text, remove_dir, write_text
from utils.links import detect_broken_internal_links
from utils.logging import log_error, log_info, log_warn
from utils.markdown import convert_md_to_html
from utils.metadata import extract_metadata_fields, load_metadata, validate_required_fields
from utils.pathing import build_relative_prefix, compute_depth, get_relative_html_path

CONTENT_DIR = PROJECT_ROOT / "content"
SOURCE_DIR = PROJECT_ROOT / "site_src"
OUTPUT_DIR = PROJECT_ROOT / "site"
PAGES_DIR = OUTPUT_DIR / "pages"
METADATA_DIR = PROJECT_ROOT / "metadata" / "content"
TEMPLATE_PATH = SOURCE_DIR / "template_page.html"


def run_structure_validation():
    validator_path = PROJECT_ROOT / "scripts" / "validate_structure.py"
    result = subprocess.run(
        [sys.executable, str(validator_path)],
        check=False,
        cwd=str(PROJECT_ROOT),
    )

    if result.returncode != 0:
        log_error("Validación estructural falló. Build detenido.")
        raise SystemExit(result.returncode)

    log_info("Validación estructural completada correctamente")


def ensure_dirs():
    ensure_dir(PAGES_DIR)


def clean_output_dir():
    if OUTPUT_DIR.exists():
        remove_dir(OUTPUT_DIR)
        log_info("Contenido previo de site/ eliminado")


def copy_static_assets():
    if not SOURCE_DIR.exists():
        raise Exception(f"No existe la carpeta fuente: {SOURCE_DIR}")

    copy_dir(SOURCE_DIR, OUTPUT_DIR)
    log_info("Archivos base copiados desde site_src/")

    assets_dir = PROJECT_ROOT / "assets"
    if assets_dir.exists():
        copy_dir(assets_dir, OUTPUT_DIR / "assets", merge=True)
        log_info("Carpeta assets/ copiada a site/assets/")


def wrap_html(title, body, depth=1):
    prefix = build_relative_prefix(depth)
    html_template = read_text(TEMPLATE_PATH)
    return (
        html_template.replace("{{TITLE}}", title)
        .replace("{{BODY}}", body)
        .replace("{{PREFIX}}", prefix)
    )


def process_markdown():
    if not CONTENT_DIR.exists():
        raise Exception("No existe la carpeta content/")

    generated_pages = []
    id_to_path = {}

    for md_path in sorted(CONTENT_DIR.rglob("*.md")):
        md_base = md_path.stem
        rel_path_html = get_relative_html_path(md_path, CONTENT_DIR)
        out_path = PAGES_DIR / rel_path_html

        ensure_dir(out_path.parent)

        depth = compute_depth(rel_path_html)
        md_text = read_text(md_path)
        html_content, conversions = convert_md_to_html(md_text)
        display_title = md_base.replace("_", " ").title()

        write_text(out_path, wrap_html(display_title, html_content, depth))

        generated_pages.append(str(out_path))
        id_to_path[md_base] = rel_path_html.replace(os.sep, "/")
        log_info(f"Archivo procesado: {md_path}")
        log_info(f"Conversión realizada: {md_path} -> {out_path}")
        if conversions:
            log_info(f"Enlaces .md corregidos: {conversions} en {out_path}")

    return generated_pages, id_to_path


def build_glossary():
    glossary_html = "<h1>Glosario de Conceptos</h1><ul>"

    if METADATA_DIR.exists():
        for path in sorted(METADATA_DIR.rglob("*.json")):
            if path.name == "schema.json":
                continue

            try:
                data = load_metadata(path)
                fields = extract_metadata_fields(data)
                for concept in fields["concepts"]:
                    glossary_html += f"<li>{concept}</li>"
            except Exception as exc:
                log_warn(f"Error leyendo metadata {path}: {exc}")

    glossary_html += "</ul>"

    out_path = OUTPUT_DIR / "glossary.html"
    write_text(out_path, wrap_html("Glosario", glossary_html, depth=0))

    log_info(f"Conversión realizada: glosario -> {out_path}")


def generate_metadata_index(id_to_path, target_path, depth=1):
    target_path = Path(target_path)
    metadata_items = []

    if not METADATA_DIR.exists():
        log_warn("No existe metadata/, no se puede construir índice por metadata")
        return

    for path in sorted(METADATA_DIR.rglob("*.json")):
        if path.name == "schema.json":
            continue

        try:
            data = load_metadata(path)
            missing = validate_required_fields(data, ["id"])
            if missing:
                log_warn(f"Metadata inválida en {path}: faltan campos {missing}")
                continue

            md_id = data["id"]
            if md_id in id_to_path:
                rel_link = id_to_path[md_id].replace(os.sep, "/")
                page_link = f"./pages/{rel_link}" if depth == 0 else f"./{rel_link}"
                fields = extract_metadata_fields(data)

                metadata_items.append(
                    {
                        "title": fields["title"] or md_id,
                        "module": fields["module"] or "zz_sin_modulo",
                        "order": fields["order"] if isinstance(fields["order"], int) else 9999,
                        "link": page_link,
                    }
                )
            else:
                log_warn(f"ID {md_id} de metadata no encontrado en archivos .md")
        except Exception as exc:
            log_warn(f"No se pudo indexar {path}: {exc}")

    metadata_items.sort(key=lambda item: (item["module"], item["order"]))

    # Group by module
    current_module = None
    list_items = ""
    for item in metadata_items:
        if item["module"] != current_module:
            if current_module is not None:
                list_items += "</ul>"
            current_module = item["module"]
            clean_module_name = re.sub(r'^\d+_', '', current_module).replace('_', ' ').title()
            list_items += f"<h3>{clean_module_name}</h3><ul>"
        
        list_items += f'<li><a href="{item["link"]}">{item["title"]}</a></li>'
    
    if current_module is not None:
        list_items += "</ul>"

    index_body = f"""
    <h1>Biblioteca Matemática</h1>
    <p>Índice completo de temas disponibles en MathKernel.</p>
    {list_items}
    """

    write_text(target_path, wrap_html("Índice de Contenidos", index_body, depth=depth))

    log_info(f"Índice generado en: {target_path}")


def validate_internal_links(generated_pages):
    broken_links = detect_broken_internal_links(generated_pages)
    for html_path, link in broken_links:
        log_warn(f"Enlace interno roto: {link} en {html_path}")


if __name__ == "__main__":
    log_info("Generando sitio...")

    run_structure_validation()
    clean_output_dir()
    copy_static_assets()
    ensure_dirs()

    pages, id_to_path = process_markdown()
    
    # Generate index in /site/index.html (home)
    generate_metadata_index(id_to_path, OUTPUT_DIR / "index.html", depth=0)
    
    # Generate index in /site/pages/index.html
    generate_metadata_index(id_to_path, PAGES_DIR / "index.html", depth=1)
    
    pages.append(str(OUTPUT_DIR / "index.html"))
    pages.append(str(PAGES_DIR / "index.html"))

    build_glossary()
    pages.append(str(OUTPUT_DIR / "glossary.html"))

    validate_internal_links(pages)

    log_info("Sitio generado correctamente en /site")
