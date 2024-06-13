import os
import json

from src.external_api import get_convert


def load_transactions(file_path: str) -> list:
    """которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, "..", file_path)

    try:
        if not os.path.exists(full_path):
            return []

        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                return data
            else:
                return []

    except (json.JSONDecodeError, IOError):
        return []


def get_amount(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    code_ = transaction["operationAmount"]["currency"]["code"]
    amount_ = transaction["operationAmount"]["amount"]
    if code_ in ("USD", "EUR"):
        return get_convert(code_, amount_)
    else:
        return amount_


if __name__ == "__main__":
    transactions = load_transactions("data/operations.json")
    print(transactions)

    amount = get_amount(
        {
            "id": 522357576,
            "state": "EXECUTED",
            "date": "2019-07-12T20:41:47.882230",
            "operationAmount": {"amount": "51463.70", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 48894435694657014368",
            "to": "Счет 38976430693692818358",
        }
    )

    print(amount)
