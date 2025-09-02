import json
from typing import List, Dict, Any
from src.logging_config import setup_logger

# Настройка логера для модуля utils
logger = setup_logger(__name__, "utils.log")


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с транзакциями.
    """
    try:
        if logger.handlers:
            logger.debug(f"Попытка чтения файла: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            if logger.handlers:
                logger.info(f"Успешно прочитано {len(data)} записей из файла {file_path}")
            return data
        else:
            if logger.handlers:
                logger.warning(f"Файл {file_path} не содержит список данных")
            return []

    except FileNotFoundError:
        if logger.handlers:
            logger.error(f"Файл не найден: {file_path}")
        return []

    except json.JSONDecodeError as e:
        if logger.handlers:
            logger.error(f"Ошибка декодирования JSON в файле {file_path}: {e}")
        return []

    except Exception as e:
        if logger.handlers:
            logger.error(f"Неожиданная ошибка при чтении файла {file_path}: {e}")
        return []
