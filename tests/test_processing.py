import pytest
from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(test_operations):
    # Фильтруем по EXECUTED
    filtered = filter_by_state(test_operations)
    assert len(filtered) == 2
    assert filtered[0]['id'] == 1
    assert filtered[1]['id'] == 3

    # Фильтруем по CANCELED
    filtered = filter_by_state(test_operations, 'CANCELED')
    assert len(filtered) == 1
    assert filtered[0]['id'] == 2

@pytest.mark.parametrize("ascending, expected_order", [
    (True, [2, 3, 1]),  # по возрастанию
    (False, [1, 3, 2])  # по убыванию
])
def test_sort_by_date(test_operations, ascending, expected_order):
    sorted_ops = sort_by_date(test_operations, ascending=ascending)
    assert [op['id'] for op in sorted_ops] == expected_order
