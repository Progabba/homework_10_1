import os
import json
import requests

def load_transactions(file_path: str) -> list:
    """которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, '..', file_path)

    try:
        if not os.path.exists(full_path):
            return []

        with open(full_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            else:
                return []

    except (json.JSONDecodeError, IOError):
        return []

def get_amount(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    return transaction['operationAmount']['amount']


if __name__ == '__main__':
    transactions = load_transactions('data/operations.json')
    print(transactions)

    amount = get_amount({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  })

    print(amount)