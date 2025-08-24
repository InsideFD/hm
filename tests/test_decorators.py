import pytest
import os
import tempfile
from src.decorators import log


def test_log_to_file():
    """Тестирование записи логов в файл"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
        tmp_filename = tmp.name

    @log(filename=tmp_filename)
    def add(a, b):
        return a + b

    # Вызываем функцию
    result = add(2, 3)
    assert result == 5

    # Проверяем запись в файл
    with open(tmp_filename, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "add ok" in content

    # Удаляем временный файл
    os.unlink(tmp_filename)


def test_log_to_console(capsys):
    """Тестирование вывода логов в консоль"""

    @log()
    def multiply(x, y):
        return x * y

    result = multiply(4, 5)
    assert result == 20

    captured = capsys.readouterr()
    assert "multiply ok" in captured.out


def test_log_error_to_file():
    """Тестирование записи ошибок в файл"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as tmp:
        tmp_filename = tmp.name

    @log(filename=tmp_filename)
    def divide(a, b):
        return a / b

    # Вызываем функцию с ошибкой
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    # Проверяем запись ошибки в файл
    with open(tmp_filename, 'r', encoding='utf-8') as f:
        content = f.read()
        assert "divide error" in content
        assert "ZeroDivisionError" in content

    os.unlink(tmp_filename)


def test_log_error_to_console(capsys):
    """Тестирование вывода ошибок в консоль"""

    @log()
    def failing_func():
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        failing_func()

    captured = capsys.readouterr()
    assert "failing_func error" in captured.out
    assert "ValueError" in captured.out
