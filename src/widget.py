from datetime import datetime


def get_mask_card(card_number: str) -> str:
    """Функция возвращает номер карты с маской"""
    str_card_number = str(card_number)
    return f"{str_card_number[:4]} {str_card_number[4:6]}{"*" * 2} {"*" * 4} {str_card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция возвращает номер счета с маской"""
    str_account_number = str(account_number)
    return f"{"*" * 2}{str_account_number[-4:]}"


def get_count_nams(nums: int | str) -> str:
    """функция которая определяет что ввели: номер карты или номер счета"""
    nums = str(nums)
    if len(nums) == 16:
        return get_mask_card(nums)
    return get_mask_account(nums)


def get_super_mask(nums: str) -> str:
    """Функция возвращает исходную строку с замаскированным номером карты/счета"""
    nums_list = nums.split()
    nums_list[-1] = get_count_nams(nums_list[-1])
    return " ".join(nums_list)


def get_changed_formate_time(date_time: str) -> str:
    isoformate_date_time = datetime.fromisoformat(date_time)
    return isoformate_date_time.strftime("%d.%m.%Y")
