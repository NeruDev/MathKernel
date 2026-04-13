import pytest

from scripts.core.error_handling import FileOperationError
from scripts.io.file_manager import FileManager


def test_file_manager_text_roundtrip(tmp_path):
    fm = FileManager()
    file_path = tmp_path / "a" / "b" / "sample.txt"

    fm.write_text(file_path, "hola")
    result = fm.read_text(file_path)

    assert result == "hola"


def test_file_manager_json_roundtrip(tmp_path):
    fm = FileManager()
    file_path = tmp_path / "data" / "sample.json"

    fm.write_json(file_path, {"id": "x"})
    result = fm.read_json(file_path)

    assert result == {"id": "x"}


def test_file_manager_missing_file_raises(tmp_path):
    fm = FileManager()
    missing = tmp_path / "missing.txt"

    with pytest.raises(FileOperationError):
        fm.read_text(missing)
