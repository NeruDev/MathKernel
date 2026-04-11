import json
import os
import re
import shutil
import subprocess
import sys

import markdown

CONTENT_DIR = "content"
SOURCE_DIR = "site_src"
OUTPUT_DIR = "site"
PAGES_DIR = os.path.join(OUTPUT_DIR, "pages")
METADATA_DIR = "metadata"


def log_info(msg):
    print(f"[INFO] {msg}")


def log_warn(msg):
    print(f"[WARN] {msg}")


def log_error(msg):
    print(f"[ERROR] {msg}")


def run_structure_validation():
    validator_path = os.path.join("scripts", "validate_structure.py")
    result = subprocess.run([sys.executable, validator_path], check=False)

    if result.returncode != 0:
        log_error("Validación estructural falló. Build detenido.")
        raise SystemExit(result.returncode)

    log_info("Validación estructural completada correctamente")


def ensure_dirs():
    os.makedirs(PAGES_DIR, exist_ok=True)


def clean_output_dir():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
        log_info("Contenido previo de site/ eliminado")


def copy_static_assets():
    if not os.path.exists(SOURCE_DIR):
        raise Exception(f"No existe la carpeta fuente: {SOURCE_DIR}")

    shutil.copytree(SOURCE_DIR, OUTPUT_DIR)
    log_info("Archivos base copiados desde site_src/")


def convert_md_to_html(md_path, depth):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html = markdown.markdown(md_text, extensions=["tables", "fenced_code", "toc"])

    # Corregir enlaces .md (incluyendo fragmentos #)
    link_replacements = len(re.findall(r'href="[^"]+\.md(?:#[^"]*)?"', html))
    html = re.sub(r'href="([^"]+)\.md(#[^"]*)?"', r'href="\1.html\2"', html)

    prefix = "../" * depth
    html = html.replace("assets/", f"{prefix}assets/")

    return html, link_replacements


def wrap_html(title, body, depth=1):
    prefix = "../" * depth

    return f"""<!DOCTYPE html>
<html lang="es" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | MathKernel</title>

    <link rel="stylesheet" href="{prefix}styles.css">
    <script defer src="{prefix}scripts.js"></script>
        <script>
            window.MathJax = {{
                tex: {{
                    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
                    processEscapes: true
                }},
                startup: {{
                    typeset: true
                }}
            }};
        </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
</head>

<body>
<div class="container">

<header>
    <h1>{title}</h1>
    <button id="theme-toggle" class="btn-theme">🌓</button>
</header>

<nav>
    <a href="{prefix}index.html" class="nav-btn">Inicio</a>
    <a href="{prefix}pages/index.html" class="nav-btn">Contenidos</a>
    <a href="{prefix}glossary.html" class="nav-btn">Glosario</a>
</nav>

<main id="md-content">
{body}
</main>

</div>
</body>
</html>"""


def process_markdown():
    if not os.path.exists(CONTENT_DIR):
        raise Exception("No existe la carpeta content/")

    generated_pages = []
    id_to_path = {}

    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if not file.endswith(".md"):
                continue

            md_path = os.path.join(root, file)
            md_base = os.path.splitext(file)[0]
            rel_path = os.path.relpath(md_path, CONTENT_DIR)
            rel_path_html = rel_path.replace(".md", ".html")
            out_path = os.path.join(PAGES_DIR, rel_path_html)

            os.makedirs(os.path.dirname(out_path), exist_ok=True)

            depth = rel_path_html.count(os.sep) + 1
            html_content, conversions = convert_md_to_html(md_path, depth)
            display_title = file.replace(".md", "").replace("_", " ").title()

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(wrap_html(display_title, html_content, depth))

            generated_pages.append(out_path)
            id_to_path[md_base] = rel_path_html
            log_info(f"Archivo procesado: {md_path}")
            log_info(f"Conversión realizada: {md_path} -> {out_path}")
            if conversions:
                log_info(f"Enlaces .md corregidos: {conversions} en {out_path}")

    return generated_pages, id_to_path


def build_glossary():
    glossary_html = "<h1>Glosario de Conceptos</h1><ul>"

    if os.path.exists(METADATA_DIR):
        for file in sorted(os.listdir(METADATA_DIR)):
            if not file.endswith(".json") or file == "schema.json":
                continue

            path = os.path.join(METADATA_DIR, file)
            try:
                with open(path, encoding="utf-8") as f:
                    data = json.load(f)
                    for concept in data.get("concepts", []):
                        glossary_html += f"<li>{concept}</li>"
            except Exception as e:
                log_warn(f"Error leyendo metadata {file}: {e}")

    glossary_html += "</ul>"

    out_path = os.path.join(OUTPUT_DIR, "glossary.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(wrap_html("Glosario", glossary_html, depth=0))

    log_info(f"Conversión realizada: glosario -> {out_path}")


def generate_metadata_index(id_to_path, target_path, depth=1):
    metadata_items = []

    if not os.path.exists(METADATA_DIR):
        log_warn("No existe metadata/, no se puede construir índice por metadata")
        return

    for file in os.listdir(METADATA_DIR):
        if not file.endswith(".json") or file == "schema.json":
            continue

        path = os.path.join(METADATA_DIR, file)
        try:
            with open(path, "r", encoding="utf-8") as metadata_file:
                data = json.load(metadata_file)

            md_id = data["id"]
            if md_id in id_to_path:
                # Link prefix relative to the target_path
                prefix = "./" if depth == 0 else "./pages/"
                if depth == 1:
                    prefix = "./"
                
                # If we are at the root (depth=0), we link to pages/
                # If we are at pages/ (depth=1), we link to ./ (current dir)
                
                rel_link = id_to_path[md_id].replace(os.sep, "/")
                if depth == 0:
                    page_link = f"./pages/{rel_link}"
                else:
                    page_link = f"./{rel_link}"
                
                metadata_items.append(
                    {
                        "title": data.get("title", data["id"]),
                        "module": data.get("module", "zz_sin_modulo"),
                        "order": data.get("order", 9999),
                        "link": page_link,
                    }
                )
            else:
                log_warn(f"ID {md_id} de metadata no encontrado en archivos .md")
        except Exception as exc:
            log_warn(f"No se pudo indexar {file}: {exc}")

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

    with open(target_path, "w", encoding="utf-8") as index_file:
        index_file.write(wrap_html("Índice de Contenidos", index_body, depth=depth))

    log_info(f"Índice generado en: {target_path}")


def detect_broken_internal_links(generated_pages):
    href_pattern = re.compile(r'href="([^"]+)"')

    for html_path in generated_pages:
        with open(html_path, "r", encoding="utf-8") as html_file:
            html_content = html_file.read()

        links = href_pattern.findall(html_content)

        for link in links:
            if (
                link.startswith("http://")
                or link.startswith("https://")
                or link.startswith("#")
                or link.startswith("mailto:")
            ):
                continue

            target = link.split("#", 1)[0]
            if not target or target.endswith(".css") or target.endswith(".js"):
                continue

            target_path = os.path.normpath(os.path.join(os.path.dirname(html_path), target))
            if not os.path.exists(target_path):
                log_warn(f"Enlace interno roto: {link} en {html_path}")


if __name__ == "__main__":
    log_info("Generando sitio...")

    run_structure_validation()
    clean_output_dir()
    copy_static_assets()
    ensure_dirs()

    pages, id_to_path = process_markdown()
    
    # Generate index in /site/index.html (home)
    generate_metadata_index(id_to_path, os.path.join(OUTPUT_DIR, "index.html"), depth=0)
    
    # Generate index in /site/pages/index.html
    generate_metadata_index(id_to_path, os.path.join(PAGES_DIR, "index.html"), depth=1)
    
    pages.append(os.path.join(OUTPUT_DIR, "index.html"))
    pages.append(os.path.join(PAGES_DIR, "index.html"))

    build_glossary()
    pages.append(os.path.join(OUTPUT_DIR, "glossary.html"))

    detect_broken_internal_links(pages)

    log_info("Sitio generado correctamente en /site")
