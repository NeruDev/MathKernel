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
    """Copia index.html, styles.css y scripts.js desde site_src a site"""
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: No se encuentra la carpeta origen {SOURCE_DIR}")
        return

    for item in os.listdir(SOURCE_DIR):
        s = os.path.join(SOURCE_DIR, item)
        d = os.path.join(OUTPUT_DIR, item)
        if os.path.isfile(s):
            shutil.copy2(s, d)
            print(f"Copiado: {item}")

def convert_md_to_html(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Soporte para tablas y extensiones comunes
    html = markdown.markdown(md_text, extensions=["tables", "fenced_code"])

    # Convertir enlaces .md → .html
    html = re.sub(r'href="([^"]+)\.md"', r'href="\1.html"', html)

    # Arreglar rutas de assets si existieran
    html = html.replace("assets/", "../assets/")

    return html

def wrap_html(title, body, depth=1):
    """Envuelve el contenido en una estructura HTML similar a index.html"""
    prefix = "../" * depth
    
    # Intentar leer el template base si fuera necesario, 
    # pero por ahora lo mantenemos hardcoded para consistencia
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
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                html_content = convert_md_to_html(md_path)

                # Nombre del archivo de salida
                name = file.replace(".md", ".html")
                out_path = os.path.join(PAGES_DIR, name)

                # Título amigable (quitando guiones bajos y capitalizando)
                display_title = file.replace(".md", "").replace("_", " ").capitalize()

                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(wrap_html(display_title, html_content, depth=1))
                print(f"Generado: {out_path}")

def build_glossary():
    glossary_html = "<h1>Glosario de Conceptos</h1><div class='glossary-list'><ul>"

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
                    print(f"Error procesando {file}: {e}")

    glossary_html += "</ul></div>"

    out_path = os.path.join(OUTPUT_DIR, "glossary.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(wrap_html("Glosario", glossary_html, depth=0))
    print(f"Generado: {out_path}")

if __name__ == "__main__":
    ensure_dirs()
    copy_static_assets()
    process_markdown()
    build_glossary()
    print("¡Sitio web generado con éxito en /site!")
