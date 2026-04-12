import shutil
from pathlib import Path


def ensure_dir(path):
    target = Path(path)
    target.mkdir(parents=True, exist_ok=True)
    return target


def remove_dir(path):
    target = Path(path)
    if target.exists() and target.is_dir():
        shutil.rmtree(target)


def copy_dir(src, dst, merge=False):
    source = Path(src)
    target = Path(dst)
    if not source.exists():
        raise FileNotFoundError(f"No existe la carpeta fuente: {source}")

    shutil.copytree(source, target, dirs_exist_ok=merge)
    return target


def read_text(path):
    return Path(path).read_text(encoding="utf-8")


def write_text(path, content):
    target = Path(path)
    ensure_dir(target.parent)
    target.write_text(content, encoding="utf-8")
    return target
