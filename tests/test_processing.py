from src.processing import filter_by_state, sort_by_date

# Тестовые данные
test_operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-03T12:00:00.000000'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-01T12:00:00.000000'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-02T12:00:00.000000'}
]


def test_filter_by_state():
    # Фильтруем по EXECUTED
    filtered = filter_by_state(test_operations)
    assert len(filtered) == 2
    assert filtered[0]['id'] == 1
    assert filtered[1]['id'] == 3

    # Фильтруем по CANCELED
    filtered = filter_by_state(test_operations, 'CANCELED')
    assert len(filtered) == 1
    assert filtered[0]['id'] == 2


def test_sort_by_date():
    # Сортировка по возрастанию
    sorted_asc = sort_by_date(test_operations, ascending=True)
    assert sorted_asc[0]['id'] == 2
    assert sorted_asc[1]['id'] == 3
    assert sorted_asc[2]['id'] == 1

    # Сортировка по убыванию
    sorted_desc = sort_by_date(test_operations, ascending=False)
    assert sorted_desc[0]['id'] == 1
    assert sorted_desc[1]['id'] == 3
    assert sorted_desc[2]['id'] == 2
