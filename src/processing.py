def filter_by_state(input_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает на вход список словарей и значение для ключа
    state (опциональный параметр со значением по умолчанию
    EXECUTED) и возвращает новый список, содержащий только те словари, у которых ключ"""
    return [i for i in input_list if i.get("state") == state]


def sorted_by_date(input_list: list, ascending: bool = True) -> list:
    """принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты (ключ date).
     Функция принимает два аргумента, второй необязательный задает
     порядок сортировки (убывание, возрастание)."""
    sorted_list = sorted(input_list, key=lambda q: q.get("date"), reverse=ascending)
    return sorted_list
