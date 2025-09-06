import pandas as pd
from typing import List, Dict, Any, cast


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл и возвращает список словарей с транзакциями.
    """
    try:
        # Читаем CSV файл
        df = pd.read_csv(file_path, sep=';')

        # Конвертируем DataFrame в список словарей и явно приводим к нужному типу
        transactions = df.to_dict('records')
        return cast(List[Dict[str, Any]], transactions)

    except Exception:
        return []


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает Excel-файл и возвращает список словарей с транзакциями.
    """
    try:
        # Читаем Excel файл
        df = pd.read_excel(file_path, engine='openpyxl')

        # Конвертируем DataFrame в список словарей и явно приводим к нужному типу
        transactions = df.to_dict('records')
        return cast(List[Dict[str, Any]], transactions)

    except Exception:
        return []
