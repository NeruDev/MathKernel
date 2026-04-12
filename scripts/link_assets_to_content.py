import json
import os
from pathlib import Path

# Configuración de rutas
PROJECT_ROOT = Path(__file__).parent.parent
# Ruta homologada: metadata/assets/images/grafics
METADATA_ASSETS_ROOT = PROJECT_ROOT / "metadata" / "assets" / "images" / "grafics"
CONTENT_ROOT = PROJECT_ROOT / "content"

# Mapeo de topic_id a archivos de content
TOPIC_TO_FILE = {
    "FUN-04": "00_fundamentos/04_geometria/geometria.md",
    "FUN-05": "00_fundamentos/05_trigonometria/trigonometria.md",
    "FUN-06": "00_fundamentos/06_geometria_analitica/geometria_analitica.md",
    "CV-01": "04_calculo_vectorial/01_vectores_en_el_espacio/vectores.md",
    "CV-03": "04_calculo_vectorial/03_funciones_vectoriales/funciones_vectoriales.md",
    "CV-04": "04_calculo_vectorial/04_funciones_de_varias_variables/funciones_de_varias_variables.md",
    "CV-05": "04_calculo_vectorial/05_integracion_multiple/integracion_multiple.md",
    "ED-01": "05_ecuaciones_diferenciales/01_edo_primer_orden/edo_primer_orden.md",
    "ED-02": "05_ecuaciones_diferenciales/02_edo_segundo_orden/edo_segundo_orden.md",
    "ED-03": "05_ecuaciones_diferenciales/04_sistemas_edo/sistemas_edo.md",
    "ED-04": "05_ecuaciones_diferenciales/03_transformada_laplace/transformada_laplace.md",
    "ED-05": "05_ecuaciones_diferenciales/05_series_de_potencias/series_de_potencias.md",
}

def get_relative_image_path(md_file_rel_path, image_path):
    """Calcula la ruta relativa desde el archivo MD a la imagen."""
    # El archivo MD está en content/<subpath>
    # La imagen está en assets/images/grafics/<subpath>
    depth = len(Path(md_file_rel_path).parts)
    prefix = "../" * depth
    return f"{prefix}{image_path}"

def main():
    if not METADATA_ASSETS_ROOT.exists():
        print(f"❌ No se encontró la carpeta de metadatos de activos en {METADATA_ASSETS_ROOT}")
        return

    # Buscar todos los archivos .json recursivamente
    asset_files = list(METADATA_ASSETS_ROOT.rglob("*.json"))
    
    if not asset_files:
        print("⚠️ No se encontraron archivos de metadatos de activos.")
        return

    for json_path in asset_files:
        with open(json_path, "r", encoding="utf-8") as f:
            asset = json.load(f)

        topic_id = asset.get("topic_id")
        if not topic_id or topic_id not in TOPIC_TO_FILE:
            print(f"⚠️ No hay mapeo para topic_id: {topic_id} en {json_path.name}")
            continue

        md_rel_path = TOPIC_TO_FILE[topic_id]
        md_full_path = CONTENT_ROOT / md_rel_path
        
        if not md_full_path.exists():
            print(f"❌ No se encontró el archivo: {md_full_path}")
            continue

        # Preparar el link de la imagen
        rel_img_path = get_relative_image_path(md_rel_path, asset["image_path"])
        img_markdown = f"\n\n![{asset['description']}]({rel_img_path})\n"
        
        # Leer el contenido actual
        with open(md_full_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Buscar la sección
        section_id = asset["section"].split(" ")[0] # Tomar solo el número ej: "4.2"
        section_found = False
        new_lines = []
        
        for line in lines:
            new_lines.append(line)
            # Buscar un encabezado que contenga el ID de sección
            # Ej: "## 4.2 Ángulos"
            if line.startswith("#") and (f" {section_id} " in line or f" {section_id}\n" in line or line.strip().endswith(f" {section_id}")):
                if not section_found:
                    new_lines.append(img_markdown)
                    section_found = True
                    print(f"✅ Insertada imagen '{asset['id']}' en {md_rel_path} (sección {section_id})")

        if not section_found:
            # Si no se encontró la sección específica, añadir al final
            new_lines.append(img_markdown)
            print(f"ℹ️ Sección {section_id} no encontrada en {md_rel_path}. Añadiendo imagen '{asset['id']}' al final.")

        # Guardar cambios
        with open(md_full_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

if __name__ == "__main__":
    main()
