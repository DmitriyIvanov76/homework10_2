from src.masks import get_mask_card_number
from src.generate_cart_namber import generate_number
import pytest


@pytest.mark.parametrize('num, res', generate_number(10, 16))

def test_get_cart_number(num, res):
    assert get_mask_card_number(num) == res

def test_get_mask_number_bad():
    with pytest.raises(ValueError):
        get_mask_card_number('1')

def test_get_cart_number_bad_second():
    with pytest.raises(ValueError):
        get_mask_card_number('')