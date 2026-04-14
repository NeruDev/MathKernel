# yaml_frontmatter:
#   id: 'validate_encoding'
#   script_path: 'scripts/validate_encoding.py'
#   metadata_path: 'metadata/scripts/validate_encoding.meta.json'
#   source_of_truth: 'metadata/scripts/**/*.meta.json'
#   title: 'Validador UTF-8 de rutas criticas del repositorio'
#   key_functions:
#     - '_targets'
#     - 'main'
#   tags:
#     - 'validacion'
#     - 'encoding'
#     - 'utf8'

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.config import Paths
from scripts.core import validators
from utils.logging import log_error, log_info


def _targets(paths: Paths) -> list[Path]:
    """Define las rutas del proyecto que deben mantenerse en UTF-8."""

    return [
        paths.content_dir,
        paths.metadata_dir,
        paths.scripts_dir,
        paths.project_root / "utils",
        paths.site_src_dir,
        paths.project_root / "docs",
        paths.project_root / "README.md",
        paths.project_root / "requirements.txt",
    ]


def main() -> int:
    """Ejecuta validacion UTF-8 y retorna codigo de salida CLI."""

    paths = Paths.from_project_root(PROJECT_ROOT)
    errors = validators.validate_utf8_targets(_targets(paths))

    if errors:
        for error in errors:
            log_error(error)
        return 1

    log_info("Validacion UTF-8 completada correctamente")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
