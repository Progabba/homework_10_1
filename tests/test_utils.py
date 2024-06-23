import os
from unittest.mock import patch, mock_open

import pandas as pd
import pytest


from src.external_api import get_convert
from src.processing import filter_by_state, sorted_by_date
from src.utils import load_transactions, load_transactions_csv
from src.widget import get_changed_formate_time, get_count_nams, get_mask_account, get_mask_card


def test_get_mask_card(simple_cart_number_conf):
    """тестирует простые карты"""
    assert get_mask_card(simple_cart_number_conf) == "7000 79** **** 6361"


def test_get_acc_number(simple_acc_number_conf):
    """тестирует простые счета"""
    assert get_mask_account(simple_acc_number_conf) == "**4305"


@pytest.mark.parametrize(
    "some_number, expected", [("7000792289606361", "7000 79** **** 6361"), ("73654108430135874305", "**4305")]
)
def test_get_count_nams(some_number, expected):
    """тестирует функцию вывода по стату"""
    assert get_count_nams(some_number) == expected


@pytest.mark.parametrize(
    "some_number, expected",
    [
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def get_super_mask(some_number, expected):
    """тестирует конечную функцию по картам и счетам"""
    assert get_count_nams(some_number) == expected


def test_formate_time(formate_time):
    """тестирует функцию про время"""
    assert get_changed_formate_time(formate_time) == "11.07.2018"


def test_filter_by_state(processing_conf):
    """тестирует функцию вывода по стату"""
    assert filter_by_state(processing_conf) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_cancel(processing_conf):
    """тестирует функцию вывода по стату, если CANCELED"""
    assert filter_by_state(processing_conf, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sorted_by_date(processing_conf):
    """тестирует функцию по дате"""
    assert sorted_by_date(processing_conf) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@patch("requests.get")
def test_get_convert(mock_get):
    mock_get.return_value.json.return_value = {"result": 1}
    assert get_convert("USD", 1) == 1
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": os.getenv("API_KEY")},
        params={"amount": 1, "from": "USD", "to": "RUB"},
    )


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]')
@patch("os.path.exists", return_value=True)
def test_load_transactions(mock_exists, mock_open_file):
    expected_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
    result = load_transactions("test_file.json")
    assert result == expected_data, f"Expected {expected_data}, but got {result}"


@patch("src.utils.pd.read_csv")
def test_load_transactions_csv(mock_read_csv):
    mock_data = pd.DataFrame([{"column1": "value1", "column2": "value2"}])
    mock_read_csv.return_value = mock_data
    assert load_transactions_csv("file_path") == [{"column1": "value1", "column2": "value2"}]


@patch("src.utils.pd.read_excel")
def load_transactions_xlsx(mock_read_excel):
    mock_data = pd.DataFrame([{"column1": "value1", "column2": "value2"}])
    mock_read_excel.return_value = mock_data
    assert load_transactions_xlsx("file_path") == [{"column1": "value1", "column2": "value2"}]
