from src.masks import get_mask_card_number, get_mask_account


def main():
    # Пример использования функций
    card = "1234567890123456"
    account = "12345678"

    print(f"Маскированная карта: {get_mask_card_number(card)}")
    print(f"Маскированный счет: {get_mask_account(account)}")


if __name__ == "__main__":
    main()
