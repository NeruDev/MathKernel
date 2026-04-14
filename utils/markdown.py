import re
import markdown

# Extension completa de pymdownx para compatibilidad con Python-Markdown.
DEFAULT_EXTENSIONS = ["tables", "fenced_code", "toc", "pymdownx.arithmatex"]
FRONTMATTER_COMMENT_RE = re.compile(r"^\s*<!--\s*yaml_frontmatter:\s*.*?-->\s*", re.DOTALL)


def strip_commented_yaml_frontmatter(md_text: str) -> str:
    """Elimina bloque YAML en comentario HTML al inicio del Markdown."""
    match = FRONTMATTER_COMMENT_RE.match(md_text)
    if not match:
        return md_text
    return md_text[match.end():].lstrip("\n")

def convert_md_to_html(md_text, extensions=None, asset_prefix=None):
    """
    Convierte Markdown a HTML y ajusta enlaces.
    
    asset_prefix: Prefijo relativo opcional para corregir rutas de imágenes/activos 
                 (ej: '../../' para compensar cambios de profundidad).
    """
    active_extensions = extensions or DEFAULT_EXTENSIONS
    content = strip_commented_yaml_frontmatter(md_text)
    html = markdown.markdown(content, extensions=active_extensions)

    # Corregir enlaces a archivos .md para que apunten a .html
    html = re.sub(r'href="([^"]+)\.md(#[^"]*)?"', r'href="\1.html\2"', html)

    # Corregir rutas de imágenes si se proporciona un prefijo
    # Mantenemos la estructura interna después de ../../../assets/
    if asset_prefix is not None:
        # El patrón busca la ruta que llega hasta assets/ y captura lo que sigue
        # Ejemplo: ../../../assets/images/grafics/file.svg -> asset_prefix + assets/images/grafics/file.svg
        html = re.sub(r'src="\.\./\.\./\.\./assets/([^"]+)"', f'src="{asset_prefix}assets/\\1"', html)
        html = re.sub(r'href="\.\./\.\./\.\./assets/([^"]+)"', f'href="{asset_prefix}assets/\\1"', html)

    replacements = len(re.findall(r'href="[^"]+\.html(?:#[^"]*)?"', html))

    return html, replacements
