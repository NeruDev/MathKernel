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
    return any(part in IGNORED_DIR_NAMES for part in path.parts)


def _iter_candidate_files(path: Path, extensions: set[str]) -> list[Path]:
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
