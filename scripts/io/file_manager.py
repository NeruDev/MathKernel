import json
import shutil
from pathlib import Path
from typing import Any

from scripts.core.error_handling import FileOperationError


class FileManager:
    def ensure_dir(self, path: str | Path) -> Path:
        target = Path(path)
        try:
            target.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            raise FileOperationError(
                f"No se pudo crear el directorio: {target}",
                context={"path": str(target)},
            ) from exc
        return target

    def read_text(self, path: str | Path) -> str:
        target = Path(path)
        try:
            return target.read_text(encoding="utf-8")
        except (FileNotFoundError, OSError, UnicodeDecodeError) as exc:
            raise FileOperationError(
                f"No se pudo leer archivo de texto: {target}",
                context={"path": str(target)},
            ) from exc

    def write_text(self, path: str | Path, content: str) -> Path:
        target = Path(path)
        self.ensure_dir(target.parent)
        try:
            target.write_text(content, encoding="utf-8")
        except (OSError, UnicodeEncodeError) as exc:
            raise FileOperationError(
                f"No se pudo escribir archivo de texto: {target}",
                context={"path": str(target)},
            ) from exc
        return target

    def read_json(self, path: str | Path) -> dict[str, Any]:
        target = Path(path)
        try:
            with target.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
        except (FileNotFoundError, OSError, json.JSONDecodeError, UnicodeDecodeError) as exc:
            raise FileOperationError(
                f"No se pudo leer JSON: {target}",
                context={"path": str(target)},
            ) from exc

        if not isinstance(data, dict):
            raise FileOperationError(
                f"El JSON debe ser un objeto en: {target}",
                context={"path": str(target)},
            )

        return data

    def write_json(self, path: str | Path, data: dict[str, Any]) -> Path:
        target = Path(path)
        self.ensure_dir(target.parent)
        try:
            with target.open("w", encoding="utf-8") as handle:
                json.dump(data, handle, indent=2, ensure_ascii=False)
        except (OSError, UnicodeEncodeError) as exc:
            raise FileOperationError(
                f"No se pudo escribir JSON: {target}",
                context={"path": str(target)},
            ) from exc

        return target

    def copy_dir(self, src: str | Path, dst: str | Path, merge: bool = False) -> Path:
        source = Path(src)
        target = Path(dst)
        if not source.exists():
            raise FileOperationError(
                f"No existe la carpeta fuente: {source}",
                context={"path": str(source)},
            )

        try:
            shutil.copytree(source, target, dirs_exist_ok=merge)
        except OSError as exc:
            raise FileOperationError(
                f"No se pudo copiar directorio {source} -> {target}",
                context={"src": str(source), "dst": str(target)},
            ) from exc

        return target

    def remove_dir(self, path: str | Path) -> None:
        target = Path(path)
        if not target.exists():
            return

        try:
            shutil.rmtree(target)
        except OSError as exc:
            raise FileOperationError(
                f"No se pudo eliminar directorio: {target}",
                context={"path": str(target)},
            ) from exc
