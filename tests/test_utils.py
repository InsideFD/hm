import tempfile
import os
from src.utils import read_json_file


def test_utils_logging():
    """Тест логирование работает в utils"""
    with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
        f.write(b'[{"test": "data"}]')
        file_path = f.name

    read_json_file(file_path)
    assert os.path.exists("logs/utils.log")
    os.unlink(file_path)


def test_utils_logging_file_not_found():
    """Тест логирования при отсутствии файла"""
    read_json_file("nonexistent_file.json")
    assert os.path.exists("logs/utils.log")


def test_utils_logging_invalid_json():
    """Тест логирования при невалидном JSON"""
    with tempfile.NamedTemporaryFile(suffix='.json', delete=False) as f:
        f.write(b'invalid json content')
        file_path = f.name

    read_json_file(file_path)
    assert os.path.exists("logs/utils.log")
    os.unlink(file_path)
