import os
import json
import logging
import pandas as pd

from src.external_api import get_convert


logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> list:
    """которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    logger.info(f"Загрузка транзакций из файла: {file_path}")
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, "..", file_path)

    try:
        if not os.path.exists(full_path):
            logger.warning(f"Файл не найден: {full_path}")
            return []

        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, list):
                logger.info(f"Успешно загружено {len(data)} транзакций")
                return data
            else:
                logger.warning(f"Файл {full_path} не содержит список транзакций")
                return []

    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"Ошибка при чтении файла {full_path}: {e}")
        return []


def get_amount(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    logger.info("Получение суммы транзакции")
    code_ = transaction["operationAmount"]["currency"]["code"]
    amount_ = transaction["operationAmount"]["amount"]
    logger.debug(f"Код валюты: {code_}, сумма: {amount_}")
    if code_ in ("USD", "EUR"):
        logger.debug(f"Конвертированная сумма: {amount_} RUB")
        return get_convert(code_, amount_)
    else:
        return amount_
def load_transactions_csv(file_path: str) -> list:
    """Функция для чтения транзакций из CSV-файла и возвращения списка словарей с данными о транзакциях."""
    logger.info(f"Загрузка транзакций из CSV файла: {file_path}")
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, "..", file_path)
    try:
        df = pd.read_csv(full_path)
        transactions = df.to_dict(orient='records')
        logger.info(f"Успешно загружено {len(transactions)} транзакций из CSV файла")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении CSV файла {file_path}: {e}")
        return []


def load_transactions_xlsx(file_path: str) -> list:
    """Функция для чтения транзакций из XLSX-файла и возвращения списка словарей с данными о транзакциях."""
    logger.info(f"Загрузка транзакций из XLSX файла: {file_path}")
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, "..", file_path)
    try:
        df = pd.read_excel(full_path, engine='openpyxl')
        transactions = df.to_dict(orient='records')
        logger.info(f"Успешно загружено {len(transactions)} транзакций из XLSX файла")
        return transactions
    except Exception as e:
        logger.error(f"Ошибка при чтении XLSX файла {file_path}: {e}")
        return []

if __name__ == "__main__":
    # transactions = load_transactions("data/operations.json")
    # print(transactions)
    #
    transactions_csv = load_transactions_csv("data/transactions.csv")
    print(transactions_csv)

    # transactions_xlsx = load_transactions_xlsx("data/transactions_excel.xlsx")
    # print(transactions_xlsx)

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
