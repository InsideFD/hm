def test_read_csv_file_success():
    """Тест успешного чтения CSV файла"""
    from src.file_reader import read_csv_file

    result = read_csv_file('data/transactions.csv')

    # Проверяем что возвращается список
    assert isinstance(result, list)

    # Если файл существует и не пустой, проверяем структуру
    if result:
        transaction = result[0]
        assert 'id' in transaction
        assert 'state' in transaction
        assert 'date' in transaction
        assert 'amount' in transaction
        assert 'currency_code' in transaction


def test_read_excel_file_success():
    """Тест успешного чтения Excel файла"""
    from src.file_reader import read_excel_file

    result = read_excel_file('data/transactions_excel.xlsx')

    # Проверяем что возвращается список
    assert isinstance(result, list)

    # Если файл существует и не пустой, проверяем структуру
    if result:
        transaction = result[0]
        assert 'id' in transaction
        assert 'state' in transaction
        assert 'date' in transaction


def test_read_nonexistent_csv_file():
    """Тест чтения несуществующего CSV файла"""
    from src.file_reader import read_csv_file
    result = read_csv_file('nonexistent_file.csv')
    assert result == []


def test_read_nonexistent_excel_file():
    """Тест чтения несуществующего Excel файла"""
    from src.file_reader import read_excel_file
    result = read_excel_file('nonexistent_file.xlsx')
    assert result == []
