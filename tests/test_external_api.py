import pytest
import requests
from unittest.mock import patch, Mock
from src.external_api import convert_amount_to_rub, API_KEY


def test_convert_rub_to_rub():
    """Тест конвертации RUB в RUB"""
    transaction = {
        'operationAmount': {
            'amount': '100.0',
            'currency': {'code': 'RUB'}
        }
    }
    result = convert_amount_to_rub(transaction)
    assert result == 100.0


@patch('src.external_api.requests.get')
def test_convert_usd_to_rub(mock_get):
    """Тест конвертации USD в RUB с моком API"""
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 75.5}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        'operationAmount': {
            'amount': '100.0',
            'currency': {'code': 'USD'}
        }
    }

    result = convert_amount_to_rub(transaction)
    assert result == 7550.0  # 100 * 75.5

    # Проверяем, что запрос отправлен с правильным API ключом
    mock_get.assert_called_once()
    args, kwargs = mock_get.call_args
    assert kwargs['headers']['apikey'] == API_KEY


@patch('src.external_api.requests.get')
def test_convert_eur_to_rub(mock_get):
    """Тест конвертации EUR в RUB с моком API"""
    mock_response = Mock()
    mock_response.json.return_value = {'rates': {'RUB': 85.3}}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        'operationAmount': {
            'amount': '50.0',
            'currency': {'code': 'EUR'}
        }
    }

    result = convert_amount_to_rub(transaction)
    assert result == 4265.0  # 50 * 85.3


@patch('src.external_api.requests.get')
def test_api_request_failure(mock_get):
    """Тест обработки ошибки API запроса"""
    # Создаем настоящий exception, а не строку
    mock_get.side_effect = requests.exceptions.ConnectionError("Connection error")

    transaction = {
        'operationAmount': {
            'amount': '100.0',
            'currency': {'code': 'USD'}
        }
    }

    with pytest.raises(ValueError, match="API request failed"):
        convert_amount_to_rub(transaction)


@patch('src.external_api.requests.get')
def test_api_http_error(mock_get):
    """Тест обработки HTTP ошибки"""
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
    mock_get.return_value = mock_response

    transaction = {
        'operationAmount': {
            'amount': '100.0',
            'currency': {'code': 'USD'}
        }
    }

    with pytest.raises(ValueError, match="API request failed"):
        convert_amount_to_rub(transaction)


def test_unsupported_currency():
    """Тест неподдерживаемой валюты"""
    transaction = {
        'operationAmount': {
            'amount': '100.0',
            'currency': {'code': 'GBP'}
        }
    }

    with pytest.raises(ValueError, match="Unsupported currency: GBP"):
        convert_amount_to_rub(transaction)


def test_invalid_amount_format():
    """Тест неверного формата суммы"""
    transaction = {
        'operationAmount': {
            'amount': 'not_a_number',
            'currency': {'code': 'RUB'}
        }
    }

    with pytest.raises(TypeError, match="Invalid amount format"):
        convert_amount_to_rub(transaction)
