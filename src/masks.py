from src.logging_config import setup_logger

# Настройка логера для модуля masks
logger = setup_logger(__name__, "masks.log")


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.
    """
    try:
        if logger.handlers:
            logger.debug(f"Маскировка номера карты: {card_number}")

        if len(card_number) == 16 and card_number.isdigit():
            result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
            if logger.handlers:
                logger.info(f"Успешная маскировка карты: {card_number} -> {result}")
            return result

        if logger.handlers:
            logger.warning(f"Некорректный номер карты для маскировки: {card_number}")
        return card_number

    except Exception as e:
        if logger.handlers:
            logger.error(f"Ошибка при маскировке карты {card_number}: {e}")
        return card_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета.
    """
    try:
        if logger.handlers:
            logger.debug(f"Маскировка номера счета: {account_number}")

        digits = ''.join(filter(str.isdigit, account_number))
        if not digits:
            if logger.handlers:
                logger.warning(f"Номер счета не содержит цифр: {account_number}")
            return account_number

        result = f"**{digits[-4:]}"
        if logger.handlers:
            logger.info(f"Успешная маскировка счета: {account_number} -> {result}")
        return result

    except Exception as e:
        if logger.handlers:
            logger.error(f"Ошибка при маскировке счета {account_number}: {e}")
        return account_number
