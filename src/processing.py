def filter_by_state(input_list: list, state: str = "EXECUTED") -> list:
    return [i for i in input_list if i.get('state') == state]

def sorted_by_date(input_list: list, ascending: bool = True) -> list:
    sorted_list = sorted(input_list, key=lambda q: q.get('date'),  reverse=ascending)
    return sorted_list

if __name__ == "__main__":
    input_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    result1 = filter_by_state(input_list)
    print(result1)

    result2 = sorted_by_date(input_list)
    print(result2)

