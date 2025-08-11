import pytest

@pytest.fixture
def test_operations():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-03T12:00:00.000000'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-01-01T12:00:00.000000'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-02T12:00:00.000000'}
    ]

@pytest.fixture
def card_test_cases():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234", "1234"),
        ("", "")
    ]

@pytest.fixture
def account_test_cases():
    return [
        ("12345678901234567890", "**7890"),
        ("123", "**123"),
        ("", "")
    ]
