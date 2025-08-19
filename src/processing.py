from typing import List, Dict


def filter_by_state(operations: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Фильтрует операции по статусу"""
    return [op for op in operations if op.get('state') == state]


def sort_by_date(operations: List[Dict], ascending: bool = True) -> List[Dict]:
    """Сортирует операции по дате"""
    return sorted(operations, key=lambda x: x['date'], reverse=not ascending)
