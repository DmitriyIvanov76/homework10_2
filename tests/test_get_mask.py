from src.masks import get_mask_card_number
from src.generate_cart_namber import generate_number
import pytest


@pytest.mark.parametrize('num, res', generate_number(10, 16))

def test_get_mask_account(num, res):
    assert get_mask_card_number(num) == res

def test_get_mask_account_bad():
    with pytest.raises(ValueError):
        get_mask_card_number('15454545454544541')

