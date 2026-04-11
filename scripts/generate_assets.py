import os
import sys
import json
import importlib.util
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt

# Añadir la raíz del proyecto al path para importar templates y otros módulos
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import templates

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

def generate_manifest(assets_data):
    """Genera el archivo manifest.json para consumo de IA."""
    manifest_path = PROJECT_ROOT / "assets" / "images" / "grafics" / "manifest.json"
    os.makedirs(manifest_path.parent, exist_ok=True)
    
    manifest = {
        "generated_at": datetime.now().isoformat(),
        "project": "MathKernel",
        "description": "Registro de activos visuales matemáticos vectoriales (SVG).",
        "assets_count": len(assets_data),
        "assets": assets_data
    }
    
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    return manifest_path

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
        print(f"❌ Error ejecutando {script_path.name}: {e}")
    
    return None, None

def main():
    print("🚀 Iniciando generación de assets vectoriales (SVG)...")
    setup_svg_styles()
    
    graphics_root = PROJECT_ROOT / "scripts" / "grafics"
    assets_root = PROJECT_ROOT / "assets" / "images" / "grafics"
    
    all_assets = []
    
    # Recorrer recursivamente scripts/grafics/
    for py_file in graphics_root.rglob("*.py"):
        # Ignorar archivos base o de utilidades
        if py_file.name in ["templates.py", "__init__.py"] or py_file.parent.name == "grafics":
            continue
            
        print(f"  - Procesando: {py_file.relative_to(graphics_root)}")
        
        # Determinar ruta de salida manteniendo estructura
        rel_path = py_file.relative_to(graphics_root)
        output_dir = assets_root / rel_path.parent
        os.makedirs(output_dir, exist_ok=True)
        
        # Ejecutar script
        fig, metadata = run_graphic_script(py_file)
        
        if fig:
            image_name = f"{py_file.stem}.svg"
            output_path = output_dir / image_name
            
            # Guardar en formato SVG
            fig.savefig(str(output_path), format='svg', bbox_inches='tight')
            plt.close(fig)
            
            # Registrar metadatos
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
            all_assets.append(asset_info)
            print(f"    ✅ Generado: {image_name}")

    # Generar manifiesto
    if all_assets:
        manifest_file = generate_manifest(all_assets)
        print(f"\n✨ Proceso completado con éxito.")
        print(f"📦 Assets generados: {len(all_assets)}")
        print(f"📄 Manifiesto creado en: {manifest_file.relative_to(PROJECT_ROOT)}")
    else:
        print("\n⚠️ No se generaron assets.")

if __name__ == "__main__":
    main()
