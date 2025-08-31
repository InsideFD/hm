def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты:
    - Для 16 цифр: возвращает в формате '1234 56** **** 3456'
    - Для других случаев возвращает строку без изменений
    """
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return card_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета:
    - Всегда возвращает последние 4 цифры с префиксом **
    - Если цифр меньше 4, все равно добавляет **
    - Для пустой строки возвращает пустую строку
    """
    digits = ''.join(filter(str.isdigit, account_number))
    return f"**{digits[-4:]}" if digits else account_number
