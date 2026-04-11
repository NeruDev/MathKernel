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

    link_replacements = len(re.findall(r'href="([^"]+)\.md"', html))
    html = re.sub(r'href="([^"]+)\.md"', r'href="\1.html"', html)

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
    <title>{title} | Arquitectura Matemática</title>

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
    <a href="{prefix}index.html">Inicio</a>
    <a href="{prefix}glossary.html">Glosario</a>
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

    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if not file.endswith(".md"):
                continue

            md_path = os.path.join(root, file)
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
            log_info(f"Archivo procesado: {md_path}")
            log_info(f"Conversión realizada: {md_path} -> {out_path}")
            if conversions:
                log_info(f"Enlaces .md corregidos: {conversions} en {out_path}")

    return generated_pages


def build_glossary():
    glossary_html = "<h1>Glosario de Conceptos</h1><ul>"

    if os.path.exists(METADATA_DIR):
        for file in os.listdir(METADATA_DIR):
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


def generate_metadata_index():
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

            page_link = f"./{data['id']}.html"
            metadata_items.append(
                {
                    "title": data.get("title", data["id"]),
                    "module": data.get("module", "zz_sin_modulo"),
                    "order": data.get("order", 9999),
                    "link": page_link,
                }
            )
        except Exception as exc:
            log_warn(f"No se pudo indexar {file}: {exc}")

    metadata_items.sort(key=lambda item: (item["module"], item["order"]))

    list_items = "\n".join(
        f'<li><strong>{item["title"]}</strong> '
        f'(<em>{item["module"]}</em>) - '
        f'<a href="{item["link"]}">Ver página</a></li>'
        for item in metadata_items
    )

    index_body = f"""
    <h1>Índice de contenidos</h1>
    <ul>
    {list_items}
    </ul>
    """

    out_path = os.path.join(PAGES_DIR, "index.html")
    with open(out_path, "w", encoding="utf-8") as index_file:
        index_file.write(wrap_html("Índice", index_body, depth=1))

    log_info(f"Conversión realizada: índice metadata -> {out_path}")


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

    pages = process_markdown()
    generate_metadata_index()
    pages.append(os.path.join(PAGES_DIR, "index.html"))

    build_glossary()
    pages.append(os.path.join(OUTPUT_DIR, "glossary.html"))

    detect_broken_internal_links(pages)

    log_info("Sitio generado correctamente en /site")
