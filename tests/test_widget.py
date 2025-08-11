import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("input_str, expected", [
    ("Visa 1234567890123456", "Visa 1234 56** **** 3456"),
    ("Счет 12345678901234567890", "Счет **7890"),
    ("", "")
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected

@pytest.mark.parametrize("date_str, expected", [
    ("2023-01-15T12:30:45.123456", "15.01.2023"),
    ("2022-12-31T23:59:59.999999", "31.12.2022")
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
