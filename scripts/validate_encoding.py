import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.config import Paths
from scripts.core import validators
from utils.logging import log_error, log_info


def _targets(paths: Paths) -> list[Path]:
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
