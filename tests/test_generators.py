import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 1"
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "EUR"}},
            "description": "Transaction 2"
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 3"
        }
    ]


def test_filter_by_currency(sample_transactions):
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions)["id"] == 1
    assert next(usd_transactions)["id"] == 3
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_transaction_descriptions(sample_transactions):
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Transaction 1"
    assert next(descriptions) == "Transaction 2"
    assert next(descriptions) == "Transaction 3"


@pytest.mark.parametrize("start,end,expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
])
def test_card_number_generator(start, end, expected):
    generator = card_number_generator(start, end)
    for expected_num in expected:
        assert next(generator) == expected_num
    with pytest.raises(StopIteration):
        next(generator)
