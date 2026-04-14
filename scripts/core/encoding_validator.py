# yaml_frontmatter:
#   id: 'encoding_validator'
#   script_path: 'scripts/core/encoding_validator.py'
#   metadata_path: 'metadata/scripts/core/encoding_validator.meta.json'
#   source_of_truth: 'metadata/scripts/**/*.meta.json'
#   title: 'Validador base de codificacion UTF-8 para archivos de texto'
#   key_functions:
#     - 'validate_utf8_file'
#     - 'validate_utf8_paths'
#   tags:
#     - 'utf8'
#     - 'validacion'
#     - 'archivos'

from pathlib import Path

DEFAULT_TEXT_EXTENSIONS = {
    ".md",
    ".json",
    ".py",
    ".html",
    ".css",
    ".js",
    ".txt",
    ".yml",
    ".yaml",
}

IGNORED_DIR_NAMES = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
}


def _is_ignored(path: Path) -> bool:
    """Indica si una ruta pertenece a directorios excluidos de escaneo."""

    return any(part in IGNORED_DIR_NAMES for part in path.parts)


def _iter_candidate_files(path: Path, extensions: set[str]) -> list[Path]:
    """Enumera archivos candidatos de texto bajo una ruta objetivo."""

    if not path.exists():
        return []

    if path.is_file():
        return [path] if path.suffix.lower() in extensions else []

    files: list[Path] = []
    for item in sorted(path.rglob("*")):
        if not item.is_file() or _is_ignored(item):
            continue
        if item.suffix.lower() in extensions:
            files.append(item)
    return files


def validate_utf8_file(path: Path) -> str | None:
    """Valida que un archivo pueda decodificarse en UTF-8."""

    try:
        path.read_bytes().decode("utf-8")
    except UnicodeDecodeError as exc:
        return (
            f"[ERROR] Codificacion no UTF-8 en {path}: "
            f"{exc.reason} (byte {exc.start})"
        )
    except OSError as exc:
        return f"[ERROR] No se pudo leer para validar UTF-8: {path} ({exc})"

    return None


def validate_utf8_paths(
    targets: list[Path],
    extensions: set[str] | None = None,
) -> list[str]:
    """Valida UTF-8 para un conjunto de targets con deduplicacion de archivos."""

    active_extensions = {ext.lower() for ext in (extensions or DEFAULT_TEXT_EXTENSIONS)}

    errors: list[str] = []
    seen: set[Path] = set()
    for target in targets:
        for file_path in _iter_candidate_files(target, active_extensions):
            if file_path in seen:
                continue
            seen.add(file_path)
            error = validate_utf8_file(file_path)
            if error:
                errors.append(error)

    return errors
