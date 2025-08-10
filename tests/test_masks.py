from src.masks import get_mask_card_number, get_mask_account


def test_mask_card_number():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number("1234") == "1234"
    assert get_mask_card_number("") == ""

def test_mask_account():
    assert get_mask_account("12345678901234567890") == "**7890"
    assert get_mask_account("123") == "**123"
    assert get_mask_account("") == ""
