from src.operations import search_by_description, count_operations_by_category


def test_search_by_description():
    """Тест поиска по описанию"""
    transactions = [
        {'description': 'Перевод организации', 'amount': 100},
        {'description': 'Покупка в магазине', 'amount': 200},
        {'description': 'Перевод другу', 'amount': 300}
    ]

    result = search_by_description(transactions, 'перевод')
    assert len(result) == 2
    assert result[0]['description'] == 'Перевод организации'
    assert result[1]['description'] == 'Перевод другу'


def test_count_operations_by_category():
    """Тест подсчета операций по категориям"""
    transactions = [
        {'description': 'Перевод организации'},
        {'description': 'Покупка в магазине'},
        {'description': 'Перевод другу'},
        {'description': 'Оплата услуг'}
    ]

    categories = ['Перевод', 'Покупка']
    result = count_operations_by_category(transactions, categories)

    assert result['Перевод'] == 2
    assert result['Покупка'] == 1
