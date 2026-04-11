import os
import markdown
import json
import re
import shutil

CONTENT_DIR = "content"
SOURCE_DIR = "site_src"
OUTPUT_DIR = "site"
PAGES_DIR = os.path.join(OUTPUT_DIR, "pages")
METADATA_DIR = "metadata"


def ensure_dirs():
    os.makedirs(PAGES_DIR, exist_ok=True)


def copy_static_assets():
    """Limpia /site y copia todo desde site_src"""
    if not os.path.exists(SOURCE_DIR):
        raise Exception(f"No existe la carpeta fuente: {SOURCE_DIR}")

    # 🔥 Limpieza total (build limpio)
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)

    shutil.copytree(SOURCE_DIR, OUTPUT_DIR)
    print("✔ Archivos base copiados")


def convert_md_to_html(md_path, depth):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc"]
    )

    # 🔗 Fix enlaces internos (.md → .html)
    html = re.sub(r'href="([^"]+)\.md"', r'href="\1.html"', html)

    # 🖼️ Fix rutas assets dinámicas
    prefix = "../" * depth
    html = html.replace("assets/", f"{prefix}assets/")

    return html


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
        raise Exception("❌ No existe la carpeta content/")

    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):

                md_path = os.path.join(root, file)

                # 🔥 Mantener estructura original
                rel_path = os.path.relpath(md_path, CONTENT_DIR)
                rel_path_html = rel_path.replace(".md", ".html")

                out_path = os.path.join(PAGES_DIR, rel_path_html)

                os.makedirs(os.path.dirname(out_path), exist_ok=True)

                depth = rel_path_html.count(os.sep) + 1

                html_content = convert_md_to_html(md_path, depth)

                # 🧠 Título limpio
                display_title = file.replace(".md", "").replace("_", " ").title()

                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(wrap_html(display_title, html_content, depth))

                print(f"✔ Generado: {out_path}")


def build_glossary():
    glossary_html = "<h1>Glosario de Conceptos</h1><ul>"

    if os.path.exists(METADATA_DIR):
        for file in os.listdir(METADATA_DIR):
            if file.endswith(".json"):
                path = os.path.join(METADATA_DIR, file)

                try:
                    with open(path, encoding="utf-8") as f:
                        data = json.load(f)

                        for concept in data.get("concepts", []):
                            glossary_html += f"<li>{concept}</li>"

                except Exception as e:
                    print(f"⚠ Error en {file}: {e}")

    glossary_html += "</ul>"

    out_path = os.path.join(OUTPUT_DIR, "glossary.html")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(wrap_html("Glosario", glossary_html, depth=0))

    print(f"✔ Generado: {out_path}")

def generate_index_links():
    links = ""

    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, file), CONTENT_DIR)
                html_path = rel_path.replace(".md", ".html")

                links += f'<li><a href="./pages/{html_path}">{file}</a></li>\n'

    return f"<ul>{links}</ul>"


if __name__ == "__main__":
    print("🚀 Generando sitio...")

    copy_static_assets()
    ensure_dirs()
    process_markdown()
    build_glossary()

    print("✅ Sitio generado correctamente en /site")