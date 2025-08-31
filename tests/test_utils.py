import json
import tempfile
import os
from src.utils import read_json_file


def test_read_json_file_valid():
    """Тест чтения валидного JSON-файла"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump([{"id": 1, "amount": 100}], f)
        file_path = f.name

    result = read_json_file(file_path)
    assert result == [{"id": 1, "amount": 100}]
    os.unlink(file_path)


def test_read_json_file_empty():
    """Тест чтения пустого файла"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        file_path = f.name

    result = read_json_file(file_path)
    assert result == []
    os.unlink(file_path)


def test_read_json_file_not_found():
    """Тест чтения несуществующего файла"""
    result = read_json_file("nonexistent.json")
    assert result == []
