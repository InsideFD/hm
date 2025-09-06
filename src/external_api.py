import requests
from typing import Dict, Any

# Константа с API ключом
API_KEY = "KU4umCOoIxWb0EOkMiSgB0pPT0iJxM7c"


def convert_amount_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными транзакции

    Returns:
        Сумма в рублях (float)

    Raises:
        ValueError: Если валюта не поддерживается или курс не найден
        TypeError: Если amount не может быть преобразован в float
    """
    try:
        amount_str = transaction['operationAmount']['amount']
        amount = float(amount_str)
    except (KeyError, ValueError, TypeError) as e:
        raise TypeError(f"Invalid amount format: {e}")

    currency = transaction['operationAmount']['currency']['code']

    if currency == 'RUB':
        return amount

    elif currency in ['USD', 'EUR']:
        url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
        headers = {"apikey": API_KEY}

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            data = response.json()
            rates = data.get('rates', {})
            rub_rate = rates.get('RUB')

            if rub_rate is None:
                raise ValueError(f"Exchange rate for RUB not found for {currency}")

            result: float = amount * rub_rate
            return round(result, 2)

        except requests.exceptions.RequestException as e:
            raise ValueError(f"API request failed: {e}")
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid API response: {e}")

    else:
        raise ValueError(f"Unsupported currency: {currency}")
