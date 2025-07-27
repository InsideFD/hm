
def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя первые 6 и последние 4 цифры видимыми.

    Args:
        card_number: Номер карты в виде строки (16 цифр)

    Returns:
        Маскированный номер карты в формате XXXX XX** **** XXXX

    Raises:
        ValueError: Если номер карты не состоит из 16 цифр
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета, оставляя последние 4 цифры видимыми.

    Args:
        account_number: Номер счета в виде строки (20 цифр)

    Returns:
        Маскированный номер счета в формате **XXXX

    Raises:
        ValueError: Если номер счета не состоит из 20 цифр
    """
    if len(account_number) != 20 or not account_number.isdigit():
        raise ValueError("Номер счета должен состоять из 20 цифр")

    return f"**{account_number[-4:]}"
