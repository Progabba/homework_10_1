from src.processing import filter_by_state, sorted_by_date
from src.utils import (
    load_transactions,
    load_transactions_csv,
    load_transactions_xlsx,
    search_operations,
    print_operations,
)
import logging


logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/main.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("\nПользователь: ")

    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        file_path = input("Введите путь к JSON-файлу: ")
        transactions = load_transactions(file_path)
        logger.info(f"Результат после нажатия 1: {transactions}")
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        file_path = input("Введите путь к CSV-файлу: ")
        transactions = load_transactions_csv(file_path)
        logger.info(f"Результат после нажатия 2: {transactions}")
    elif choice == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        file_path = input("Введите путь к XLSX-файлу: ")
        transactions = load_transactions_xlsx(file_path)
        logger.info(f"Результат после нажатия 3: {transactions}")
    else:
        print("Программа: Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")
        return

    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            "\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n\nПользователь: "
        ).upper()

        if status in valid_statuses:
            print(f'Программа: Операции отфильтрованы по статусу "{status.upper()}"')
            break
        else:
            print(f'Программа: Статус операции "{status.upper()}" недоступен.')
            print(
                "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            )
    filtered_transactions = filter_by_state(transactions, status)
    logger.info(f"Результат после фильтрации по статусу: {filtered_transactions}")

    sort_option = input("\nПрограмма: Отсортировать операции по дате? Да/Нет\n\nПользователь: ").lower()
    if sort_option == "да":
        sort_order = input("\nПрограмма: Отсортировать по возрастанию или по убыванию?\n\nПользователь: ").lower()
        ascending = True if sort_order == "по возрастанию" else False
        filtered_transactions = sorted_by_date(filtered_transactions, ascending)

    ruble_option = input("\nПрограмма: Выводить только рублевые транзакции? Да/Нет\n\nПользователь: ").lower()
    if ruble_option == "да":
        filtered_transactions = [
            transaction
            for transaction in filtered_transactions
            if transaction["operationAmount"]["currency"]["code"] == "RUB"
        ]

    keyword_option = input(
        "\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n\nПользователь: "
    ).lower()
    if keyword_option == "да":
        keyword = input("\nВведите ключевое слово для фильтрации: ")
        filtered_transactions = search_operations(filtered_transactions, keyword)

    print_operations(filtered_transactions)


if __name__ == "__main__":
    main()

    # usd_transactions = filter_by_currency(transactions, "USD")
    # for _ in range(2):
    #     print(next(usd_transactions)["id"])
    #
    # descriptions = transaction_descriptions(transactions)
    # for _ in range(5):
    #     print(next(descriptions))
    #
    # for card_number in card_number_generator(1, 5):
    #     print(card_number)
