import json
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.io import read_text, write_text
from utils.logging import log_error, log_info, log_warn
from utils.metadata import load_metadata
from utils.pathing import build_relative_prefix, compute_depth

# Configuración de rutas
METADATA_CONTENT_ROOT = PROJECT_ROOT / "metadata" / "content"
METADATA_ASSETS_ROOT = PROJECT_ROOT / "metadata" / "assets" / "images" / "grafics"
CONTENT_ROOT = PROJECT_ROOT / "content"

def get_relative_image_path(md_file_rel_path, image_path):
    """Calcula la ruta relativa desde el archivo MD a la imagen."""
    depth = compute_depth(md_file_rel_path)
    prefix = build_relative_prefix(depth)
    return f"{prefix}{image_path}"

def build_script_to_md_map():
    """Construye un mapa de nombre de script a ruta de archivo .md."""
    script_to_md = {}
    
    # Buscar todos los archivos de metadatos de contenido
    content_meta_files = list(METADATA_CONTENT_ROOT.rglob("*.json"))
    
    for meta_path in content_meta_files:
        if meta_path.name == "schema.json":
            continue
            
        data = load_metadata(meta_path)
        scripts = data.get("scripts", [])
        
        # El archivo .md está en el mismo nivel de carpeta en CONTENT_ROOT
        rel_dir = meta_path.parent.relative_to(METADATA_CONTENT_ROOT)
        target_content_dir = CONTENT_ROOT / rel_dir
        
        md_files = list(target_content_dir.glob("*.md"))
        if not md_files:
            continue
            
        md_rel_path = str(md_files[0].relative_to(CONTENT_ROOT)).replace(os.sep, "/")
        
        for script in scripts:
            # Normalizar nombre del script (quitar extensión)
            script_id = Path(script).stem
            script_to_md[script_id] = md_rel_path
            
    return script_to_md

def main():
    if not METADATA_ASSETS_ROOT.exists():
        log_error(f"No se encontró la carpeta de metadatos de activos en {METADATA_ASSETS_ROOT}")
        return

    # Construir mapa de vinculación automática
    script_to_md = build_script_to_md_map()
    log_info(f"Mapa de scripts construido con {len(script_to_md)} entradas.")

    # Buscar todos los archivos .json de activos recursivamente
    asset_files = list(METADATA_ASSETS_ROOT.rglob("*.json"))
    
    if not asset_files:
        log_warn("No se encontraron archivos de metadatos de activos.")
        return

    log_info(f"Iniciando vinculación inteligente de {len(asset_files)} activos...")

    linked_count = 0
    skipped_count = 0

    for json_path in asset_files:
        asset = load_metadata(json_path)
        asset_id = asset.get("id")

        if asset_id not in script_to_md:
            # Intentar búsqueda por topic si no hay script (fallback para escalabilidad futura)
            category = asset.get("category")
            topic = asset.get("topic")
            # ... (opcional: lógica extra de búsqueda)
            skipped_count += 1
            continue

        md_rel_path = script_to_md[asset_id]
        md_full_path = CONTENT_ROOT / md_rel_path
        
        if not md_full_path.exists():
            log_error(f"Archivo de contenido no encontrado: {md_full_path}")
            continue
            
        # Preparar el link de la imagen
        rel_img_path = get_relative_image_path(md_rel_path, asset["image_path"])
        img_markdown = f"![{asset['description']}]({rel_img_path})"
        
        # Leer el contenido actual
        raw_content = read_text(md_full_path)
        
        # Evitar duplicados por ruta
        if rel_img_path in raw_content:
            continue

        lines = raw_content.splitlines(keepends=True)

        # Buscar la sección (ej: "4.2")
        section_id = asset.get("section", "").split(" ")[0]
        section_found = False
        new_lines = []
        
        for line in lines:
            new_lines.append(line)
            # Buscar un encabezado que contenga el ID de sección
            if section_id and section_id != "N/A" and line.startswith("#") and \
               (f" {section_id} " in line or f" {section_id}\n" in line or line.strip().endswith(f" {section_id}")):
                if not section_found:
                    new_lines.append(f"\n{img_markdown}\n")
                    section_found = True
                    linked_count += 1
                    log_info(f"Vinculado: {asset_id} -> {md_rel_path} (sección {section_id})")

        if not section_found:
            # Añadir al final si no se encontró sección
            if not new_lines[-1].endswith("\n"):
                new_lines[-1] += "\n"
            new_lines.append(f"\n{img_markdown}\n")
            linked_count += 1
            log_warn(f"Sección {section_id} no hallada en {md_rel_path}. Añadido al final.")

        # Guardar cambios
        write_text(md_full_path, "".join(new_lines))

    log_info(f"Proceso completado: {linked_count} vinculados, {skipped_count} omitidos.")

if __name__ == "__main__":
    main()
