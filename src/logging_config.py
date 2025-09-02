import logging
from pathlib import Path


def setup_logger(name: str, log_file: str, level: int = logging.DEBUG) -> logging.Logger:
    """
    Настройка логера для модуля.

    Args:
        name: Имя логера (обычно __name__ модуля)
        log_file: Имя файла для записи логов
        level: Уровень логирования

    Returns:
        Настроенный объект логера
    """
    # Создаем логер
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Очищаем существующие handlers
    if logger.handlers:
        logger.handlers.clear()

    # Создаем file handler (без автосоздания папки)
    log_path = Path("logs") / log_file
    try:
        file_handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    except FileNotFoundError:
        # Если папки logs нет - возвращаем логер без handler
        return logger

    file_handler.setLevel(level)

    # Создаем форматтер
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)

    # Добавляем handler к логеру
    logger.addHandler(file_handler)

    return logger
