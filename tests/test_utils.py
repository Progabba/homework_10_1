import pytest

from src.processing import filter_by_state, sorted_by_date
from src.widget import get_changed_formate_time, get_count_nams, get_mask_account, get_mask_card
from tests.conftest import simple_acc_number_conf, simple_cart_number_conf


def test_get_mask_card(simple_cart_number_conf):
    assert get_mask_card(simple_cart_number_conf) == "7000 79** **** 6361"


def test_get_acc_number(simple_acc_number_conf):
    assert get_mask_account(simple_acc_number_conf) == "**4305"


@pytest.mark.parametrize(
    "some_number, expected", [("7000792289606361", "7000 79** **** 6361"), ("73654108430135874305", "**4305")]
)
def test_get_count_nams(some_number, expected):
    assert get_count_nams(some_number) == expected


@pytest.mark.parametrize(
    "some_number, expected",
    [
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def get_super_mask(some_number, expected):
    assert get_count_nams(some_number) == expected


def test_formate_time(formate_time):
    assert get_changed_formate_time(formate_time) == "11.07.2018"


def test_filter_by_state(processing_conf):
    assert filter_by_state(processing_conf) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state(processing_conf):
    assert filter_by_state(processing_conf, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_sorted_by_date(processing_conf):
    assert sorted_by_date(processing_conf) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
