import logging
from datetime import datetime


logger = logging.getLogger("widget")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/widget.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card(card_number: str) -> str:
    """Функция возвращает номер карты с маской"""
    logger.info("Получение маски для номера карты")
    str_card_number = str(card_number)
    masked_card_number = f"{str_card_number[:4]} {str_card_number[4:6]}{'*' * 2} {'*' * 4} {str_card_number[-4:]}"
    logger.debug(f"Замаскированный номер карты: {masked_card_number}")
    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Функция возвращает номер счета с маской"""
    logger.info("Получение маски для номера счета")
    str_account_number = str(account_number)
    masked_account_number = f"{'*' * 2}{str_account_number[-4:]}"
    logger.debug(f"Замаскированный номер счета: {masked_account_number}")
    return masked_account_number


def get_count_nams(nums: int | str) -> str:
    """функция которая определяет что ввели: номер карты или номер счета"""
    logger.info("Определение типа номера (карта или счет)")
    nums = str(nums)
    if len(nums) == 16:
        logger.debug("Определен номер карты")
        return get_mask_card(nums)
    logger.debug("Определен номер счета")
    return get_mask_account(nums)


def get_super_mask(nums: str) -> str:
    """Функция возвращает исходную строку с замаскированным номером карты/счета"""
    logger.info("Получение супер маски для строки")
    nums_list = nums.split()
    nums_list[-1] = get_count_nams(nums_list[-1])
    masked_str = " ".join(nums_list)
    logger.debug(f"Замаскированная строка: {masked_str}")
    return masked_str


def get_changed_formate_time(date_time: str) -> str:
    logger.info("Изменение формата времени")
    isoformate_date_time = datetime.fromisoformat(date_time)
    formatted_date_time = isoformate_date_time.strftime("%d.%m.%Y")
    logger.debug(f"Форматированное время: {formatted_date_time}")
    return formatted_date_time


if __name__ == "__main__":
    logger.info("Запуск программы")
    print(get_mask_card("1234567812345678"))
    print(get_mask_account("12345678"))
    print(get_count_nams("1234567812345678"))
    print(get_super_mask("1234 5678 1234 5678"))
    print(get_changed_formate_time("2023-06-16T10:15:30"))
    logger.info("Завершение программы")
