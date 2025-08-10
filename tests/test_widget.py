from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card("Visa 1234567890123456") == "Visa 1234 56** **** 3456"
    assert mask_account_card("Счет 12345678901234567890") == "Счет **7890"
    assert mask_account_card("") == ""


def test_get_date():
    assert get_date("2023-01-15T12:30:45.123456") == "15.01.2023"

    assert get_date("2022-12-31T23:59:59.999999") == "31.12.2022"
