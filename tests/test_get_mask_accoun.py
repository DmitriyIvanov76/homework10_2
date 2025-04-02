import pytest

from src.generate_cart_namber import generate_number_account
from src.masks import get_mask_account


# добавляем в параметризацию функцию генерации счетов и их маскировки
@pytest.mark.parametrize("account_num, res", generate_number_account(20, 20))
def test_get_mask_account(account_num, res):
    assert get_mask_account(account_num) == res


def test_get_mask_account_fixture(account_number_fixture):
    assert get_mask_account(account_number_fixture) == "**5555"


