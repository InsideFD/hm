from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в строке.
    Если строка пустая или не содержит номера, возвращает как есть.
    """
    if not data:
        return data

    parts = data.split()
    if len(parts) < 2:
        return data

    if data.startswith("Счет"):
        account_number = parts[-1]
        masked_number = get_mask_account(account_number)
        return f"Счет {masked_number}"
    else:
        card_number = parts[-1]
        masked_number = get_mask_card_number(card_number)
        return " ".join(parts[:-1] + [masked_number])


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат DD.MM.YYYY.

    Args:
        date_str: Дата в формате "2024-03-11T02:26:18.671407"

    Returns:
        Дата в формате "11.03.2024"
    """
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"
