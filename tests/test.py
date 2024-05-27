from src.widget import get_mask_card, get_mask_account, get_count_nams
import pytest

from tests.conftest import simple_cart_number_conf, simple_acc_number_conf


def test_get_mask_card(simple_cart_number_conf):
    assert get_mask_card(simple_cart_number_conf) == '7000 79** **** 6361'

def test_get_acc_number(simple_acc_number_conf):
    assert get_mask_account(simple_acc_number_conf) == '**4305'


#@pytest.mark.parametrize("some_number, expected", [(simple_cart_number_conf, '7000 79** **** 6361'), (simple_acc_number_conf, '**4305')])
@pytest.mark.parametrize("some_number, expected", [('7000792289606361', '7000 79** **** 6361'), ('73654108430135874305', '**4305')])
def test_get_count_nams(some_number, expected):
    assert get_count_nams(some_number) == expected