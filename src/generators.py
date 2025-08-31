from typing import Dict, List, Iterator, Generator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор.

    Args:
        transactions: Список транзакций (словарей)
        currency: Код валюты для фильтрации (например, "USD")

    Yields:
        Транзакции с указанной валютой
    """
    for transaction in transactions:
        op_amount = transaction.get("operationAmount", {})
        curr = op_amount.get("currency", {}).get("code")
        if curr == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """
    Генератор описаний транзакций.

    Args:
        transactions: Список транзакций (словарей)

    Yields:
        Описание каждой транзакции
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """
    Генератор номеров карт в заданном диапазоне.

    Args:
        start: Начальный номер карты (1-9999999999999999)
        end: Конечный номер карты (>= start)

    Yields:
        Номера карт в формате "XXXX XXXX XXXX XXXX"
    """
    for num in range(start, end + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:16]
