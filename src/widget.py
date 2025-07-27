from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в строке, содержащей тип и номер.

    Args:
        data: Строка формата "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"

    Returns:
        Строка с замаскированным номером карты или счета

    Raises:
        ValueError: Если строка не соответствует ожидаемому формату
    """
    parts = data.split()
    if len(parts) < 2:
        raise ValueError("Неверный формат входных данных")

    # Проверяем, является ли последняя часть номером (только цифры)
    if not parts[-1].isdigit():
        raise ValueError("Номер карты/счета должен содержать только цифры")

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