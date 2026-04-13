import os
import sys
import json
import importlib.util
from pathlib import Path
import matplotlib.pyplot as plt

# Añadir la raíz del proyecto al path para importar templates y otros módulos
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import templates
from utils.io import ensure_dir
from utils.logging import log_error, log_info, log_warn

def setup_svg_styles():
    """Configura estilos globales para salida SVG de alta calidad."""
    templates.setup_style()
    plt.rcParams.update({
        'svg.fonttype': 'path',  # Renderiza texto como trazados para máxima compatibilidad
        'savefig.format': 'svg',
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.1,
        'figure.autolayout': False
    })

def generate_asset_metadata(asset_data):
    """Genera archivos JSON individuales para cada activo gráfico."""
    img_path = Path(asset_data["image_path"])
    # Relativo a assets/images/grafics/
    rel_parts = img_path.parts[3:-1]
    
    # Ruta homologada con assets/images/grafics/
    metadata_root = PROJECT_ROOT / "metadata" / "assets" / "images" / "grafics"
    dest_dir = metadata_root.joinpath(*rel_parts)
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    dest_file = dest_dir / f"{asset_data['id']}.json"
    
    with open(dest_file, "w", encoding="utf-8") as f:
        json.dump(asset_data, f, indent=2, ensure_ascii=False)
    
    return dest_file

def run_graphic_script(script_path):
    """Importa y ejecuta la función generate() de un script específico."""
    module_name = script_path.stem
    spec = importlib.util.spec_from_file_location(module_name, str(script_path))
    module = importlib.util.module_from_spec(spec)
    
    try:
        spec.loader.exec_module(module)
        if hasattr(module, 'generate'):
            fig = module.generate()
            metadata = getattr(module, 'METADATA', {})
            return fig, metadata
    except Exception as e:
        log_error(f"Error ejecutando {script_path.name}: {e}")
    
    return None, None

def main():
    log_info("Iniciando generacion de assets vectoriales (SVG)...")
    setup_svg_styles()
    
    graphics_root = PROJECT_ROOT / "scripts" / "grafics"
    assets_root = PROJECT_ROOT / "assets" / "images" / "grafics"
    
    generated_count = 0
    failed_count = 0
    
    # Recorrer recursivamente scripts/grafics/
    for py_file in graphics_root.rglob("*.py"):
        # Ignorar archivos base o de utilidades
        if py_file.name in ["templates.py", "__init__.py"] or py_file.parent.name == "grafics":
            continue
            
        log_info(f"Procesando: {py_file.relative_to(graphics_root)}")
        
        # Determinar ruta de salida manteniendo estructura
        rel_path = py_file.relative_to(graphics_root)
        output_dir = assets_root / rel_path.parent
        ensure_dir(output_dir)
        
        # Ejecutar script
        fig, metadata = run_graphic_script(py_file)
        
        if fig:
            image_name = f"{py_file.stem}.svg"
            output_path = output_dir / image_name
            
            # Guardar en formato SVG
            fig.savefig(str(output_path), format='svg', bbox_inches='tight')
            plt.close(fig)
            
            # Registrar metadatos individuales en la ruta homologada
            asset_info = {
                "id": metadata.get("name", py_file.stem),
                "category": rel_path.parts[0],
                "topic": rel_path.parts[1] if len(rel_path.parts) > 2 else rel_path.parts[0],
                "topic_id": metadata.get("topic_id", "Unknown"),
                "script_source": str(py_file.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                "image_path": str(output_path.relative_to(PROJECT_ROOT)).replace("\\", "/"),
                "description": metadata.get("description", "Sin descripción"),
                "used_in": metadata.get("used_in", []),
                "section": metadata.get("section", "N/A"),
                "format": "SVG (Vectorial)"
            }
            generate_asset_metadata(asset_info)
            generated_count += 1
            log_info(f"Generado: {image_name}")
        else:
            failed_count += 1

    if generated_count and not failed_count:
        log_info("Proceso completado con exito.")
        log_info(f"Assets generados y metadatos segmentados: {generated_count}")
        return 0

    if failed_count:
        log_error(f"Se detectaron fallos en {failed_count} scripts de graficos.")
        log_info(f"Assets generados parcialmente: {generated_count}")
        return 1

    log_warn("No se generaron assets.")
    return 1

if __name__ == "__main__":
    sys.exit(main())
