from typing import Dict, Any
from src.utils import read_json_file
from src.file_reader import read_csv_file, read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.operations import search_by_description
from src.external_api import convert_amount_to_rub
from src.masks import get_mask_card_number, get_mask_account


def display_transaction(transaction: Dict[str, Any]) -> None:
    """Отображает информацию о транзакции в читаемом формате."""
    if 'date' in transaction:
        date = transaction['date'][:10]  # Берем только дату без времени
    else:
        date = 'Нет даты'

    description = transaction.get('description', 'Без описания')

    # Маскировка номера карты/счета
    from_account = transaction.get('from', '')
    to_account = transaction.get('to', '')

    if from_account.startswith('Счет'):
        from_display = get_mask_account(from_account.split()[-1])
        from_display = f"Счет {from_display}"
    elif from_account:
        from_display = get_mask_card_number(from_account.split()[-1])
        from_display = f"{' '.join(from_account.split()[:-1])} {from_display}"
    else:
        from_display = "Не указано"

    if to_account.startswith('Счет'):
        to_display = get_mask_account(to_account.split()[-1])
        to_display = f"Счет {to_display}"
    elif to_account:
        to_display = get_mask_card_number(to_account.split()[-1])
        to_display = f"{' '.join(to_account.split()[:-1])} {to_display}"
    else:
        to_display = "Не указано"

    # Конвертация суммы в рубли
    amount = convert_amount_to_rub(transaction)

    print(f"\n{date} {description}")
    if from_account:
        print(f"От: {from_display}")
    if to_account:
        print(f"Кому: {to_display}")
    print(f"Сумма: {amount:.2f} руб.")


def main() -> None:
    """Основная функция программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор файла
    while True:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Ваш выбор: ").strip()

        if choice == '1':
            transactions = read_json_file('data/operations.json')
            print("Для обработки выбран JSON-файл.")
            break
        elif choice == '2':
            transactions = read_csv_file('data/transactions.csv')
            print("Для обработки выбран CSV-файл.")
            break
        elif choice == '3':
            transactions = read_excel_file('data/transactions_excel.xlsx')
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    # Фильтрация по статусу
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}")

        status = input("Статус: ").strip().upper()

        if status in valid_statuses:
            filtered_transactions = filter_by_state(transactions, status)
            print(f"Операции отфильтрованы по статусу \"{status}\"")
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")

    # Дополнительная фильтрация
    # Сортировка по дате
    sort_choice = input("\nОтсортировать операции по дате? (Да/Нет): ").strip().lower()
    if sort_choice in ['да', 'yes', 'y', 'д']:
        order_choice = input("Отсортировать по возрастанию или по убыванию? (возрастанию/убыванию): ").strip().lower()
        ascending = order_choice in ['возрастанию', 'ascending', 'возрастание', 'asc']
        filtered_transactions = sort_by_date(filtered_transactions, ascending=ascending)

    # Фильтрация по рублевым транзакциям
    rub_only = input("\nВыводить только рублевые транзакции? (Да/Нет): ").strip().lower()
    if rub_only in ['да', 'yes', 'y', 'д']:
        filtered_transactions = [t for t in filtered_transactions
                                 if t.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']

    # Поиск по описанию
    search_choice = input(
        "\nОтфильтровать список транзакций по определенному слову в описании? (Да/Нет): ").strip().lower()
    if search_choice in ['да', 'yes', 'y', 'д']:
        search_word = input("Введите слово для поиска: ").strip()
        filtered_transactions = search_by_description(filtered_transactions, search_word)

    # Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")

    if filtered_transactions:
        for transaction in filtered_transactions:
            display_transaction(transaction)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
