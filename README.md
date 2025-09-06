# Банковский виджет операций

## Описание:

Проект для обработки и отображения банковских операций клиента в личном кабинете.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/InsideFD/hm
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.


## Тестирование

### Запуск тестов
```bash
pytest tests/
```

### Фикстуры
- `card_numbers()` - тестовые данные для номеров карт
- `account_numbers()` - тестовые данные для номеров счетов

### Параметризованные тесты
Тесты используют параметризацию для проверки:
- Корректных номеров карт/счетов
- Некорректных данных (не цифры)

## Покрытие тестами

Для генерации отчёта:
```bash
pytest --cov=src --cov-report=html
```

Отчёт будет доступен в `htmlcov/index.html`

## Модуль generators

### Функции:

#### `filter_by_currency(transactions, currency)`
Фильтрует транзакции по валюте.

```python
usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))
```

`transaction_descriptions(transactions)` - Генерирует описания транзакций.

`card_number_generator(start, end)` - Генерирует номера карт в диапазоне.

## Модуль decorators

### Декоратор `log`

Декоратор для логирования работы функций.

#### Использование:
```
from src.decorators import log

@log(filename="app.log")
def my_function(x, y):
    return x + y

# Или для вывода в консоль:
@log()
def another_function():
    return "result"
```

## Модуль utils
- `read_json_file()` - чтение JSON-файла с транзакциями

## Модуль external_api  
- `convert_amount_to_rub()` - конвертация валют в рубли

## Тестирование
```bash
pytest tests/ --cov=src/
```

## Логирование

Модули используют библиотеку `logging` для записи логов в папку `logs/`:

## Поддержка CSV и Excel файлов

### Новые функции в модуле `file_reader`:

#### `read_csv_file(file_path)`
Чтение транзакций из CSV файла.

```python
from src.file_reader import read_csv_file
transactions = read_csv_file('data/transactions.csv')
```
#### `read_excel_file(file_path)`
Чтение транзакций из Excel файла.

```python
from src.file_reader import read_excel_file
transactions = read_excel_file('data/transactions_excel.xlsx')
```