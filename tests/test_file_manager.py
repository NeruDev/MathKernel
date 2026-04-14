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


def test_file_manager_text_roundtrip_with_symbols(tmp_path):
    fm = FileManager()
    file_path = tmp_path / "utf8.txt"
    text = "Matematica: pi=3.14159265359, lambda=\u03bb, enie=\u00f1"

    fm.write_text(file_path, text)

    assert fm.read_text(file_path) == text


def test_file_manager_invalid_utf8_text_raises(tmp_path):
    fm = FileManager()
    bad_file = tmp_path / "bad.txt"
    bad_file.write_bytes(b"\xff\xfe\xfa")

    with pytest.raises(FileOperationError):
        fm.read_text(bad_file)


def test_file_manager_invalid_utf8_json_raises(tmp_path):
    fm = FileManager()
    bad_json = tmp_path / "bad.json"
    bad_json.write_bytes(b"\xff\xfe\xfa")

    with pytest.raises(FileOperationError):
        fm.read_json(bad_json)
