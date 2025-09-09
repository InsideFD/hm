import re
from collections import Counter
from typing import List, Dict, Any


def search_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """
    Ищет транзакции по заданной строке в описании с использованием регулярных выражений.

    Args:
        transactions: Список транзакций
        search_string: Строка для поиска в описании

    Returns:
        Список транзакций, содержащих строку в описании
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [t for t in transactions if 'description' in t and pattern.search(t['description'])]


def count_operations_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям.

    Args:
        transactions: Список транзакций
        categories: Список категорий для подсчета

    Returns:
        Словарь с количеством операций по категориям
    """
    category_counter: Counter[str] = Counter()

    for transaction in transactions:
        if 'description' in transaction:
            description = transaction['description'].lower()
            for category in categories:
                if category.lower() in description:
                    category_counter[category] += 1
                    break

    return dict(category_counter)
