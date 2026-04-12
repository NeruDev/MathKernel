import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from utils.logging import log_error, log_info
from utils.metadata import load_metadata

# Configuración de directorios
CONTENT_DIR = PROJECT_ROOT / "content"
ASSETS_DIR = PROJECT_ROOT / "assets" / "images" / "grafics"
METADATA_CONTENT_DIR = PROJECT_ROOT / "metadata" / "content"
METADATA_ASSETS_DIR = PROJECT_ROOT / "metadata" / "assets" / "images" / "grafics"

# Esquemas de validación
SCHEMAS_DIR = PROJECT_ROOT / "metadata" / "schemas"
CONTENT_SCHEMA_PATH = SCHEMAS_DIR / "content.schema.json"
ASSETS_SCHEMA_PATH = SCHEMAS_DIR / "assets.schema.json"

def find_files(base_dir: str, extension: str):
    paths = []
    if not os.path.exists(base_dir):
        return paths

    for root, _, files in os.walk(base_dir):
        for name in files:
            if name.endswith(extension):
                paths.append(os.path.join(root, name))

    return paths

def load_schema(path):
    if not os.path.exists(path):
        return None
    return load_metadata(path)

def validate_against_schema(data, schema, file_path):
    errors = []
    if not schema:
        return errors

    # Validación básica de campos requeridos
    required = schema.get("required", [])
    for field in required:
        if field not in data:
            errors.append(f"Falta campo requerido '{field}' en {file_path}")
        
    # Validación de tipos básica
    props = schema.get("properties", {})
    for field, value in data.items():
        if field in props:
            expected_type = props[field].get("type")
            if expected_type == "string" and not isinstance(value, str):
                errors.append(f"Campo '{field}' debe ser string en {file_path}")
            elif expected_type == "array" and not isinstance(value, list):
                errors.append(f"Campo '{field}' debe ser array en {file_path}")

    return errors

def validate_theory_structure():
    """Valida la correspondencia content <-> metadata/content."""
    errors = []
    md_files = find_files(CONTENT_DIR, ".md")
    json_files = find_files(METADATA_CONTENT_DIR, ".json")
    
    schema = load_schema(CONTENT_SCHEMA_PATH)

    md_by_rel = {os.path.relpath(p, CONTENT_DIR).replace(".md", ""): p for p in md_files}
    json_by_rel = {os.path.relpath(p, METADATA_CONTENT_DIR).replace(".json", ""): p for p in json_files}

    for rel_base, md_path in md_by_rel.items():
        if rel_base not in json_by_rel:
            errors.append(f"[ERROR] Sin metadata para: {md_path} (esperado {METADATA_CONTENT_DIR}/{rel_base}.json)")

    for rel_base, json_path in json_by_rel.items():
        if rel_base not in md_by_rel:
            errors.append(f"[ERROR] Metadata sin contenido: {json_path} (esperado {CONTENT_DIR}/{rel_base}.md)")
        else:
            data = load_metadata(json_path)
            errors.extend(validate_against_schema(data, schema, json_path))

    return errors

def validate_assets_structure():
    """Valida la correspondencia assets <-> metadata/assets/images/grafics."""
    errors = []
    img_files = find_files(ASSETS_DIR, ".svg")
    json_files = find_files(METADATA_ASSETS_DIR, ".json")
    
    schema = load_schema(ASSETS_SCHEMA_PATH)

    img_by_rel = {os.path.relpath(p, ASSETS_DIR).replace(".svg", ""): p for p in img_files}
    json_by_rel = {os.path.relpath(p, METADATA_ASSETS_DIR).replace(".json", ""): p for p in json_files}

    for rel_base, img_path in img_by_rel.items():
        if rel_base not in json_by_rel:
            errors.append(f"[ERROR] Sin metadata para imagen: {img_path} (esperado {METADATA_ASSETS_DIR}/{rel_base}.json)")

    for rel_base, json_path in json_by_rel.items():
        if rel_base not in img_by_rel:
            errors.append(f"[ERROR] Metadata de activo sin imagen: {json_path} (esperado {ASSETS_DIR}/{rel_base}.svg)")
        else:
            data = load_metadata(json_path)
            errors.extend(validate_against_schema(data, schema, json_path))

    return errors

def main():
    # Asegurar salida UTF-8 en Windows si es posible
    if sys.platform == "win32":
        try:
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
        except:
            pass

    log_info("Iniciando validacion de estructura completa...")
    
    theory_errors = validate_theory_structure()
    assets_errors = validate_assets_structure()
    
    all_errors = theory_errors + assets_errors

    if all_errors:
        log_error(f"Se encontraron {len(all_errors)} errores de validacion:")
        for err in all_errors:
            log_error(err)
        return 1

    log_info("Estructura y esquemas validados correctamente.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
