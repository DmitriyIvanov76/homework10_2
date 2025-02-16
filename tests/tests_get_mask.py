from src.masks import get_mask_account
import pytest

@pytest.mark.parametrize('cart_number, res', [
    ('4276155447963216', '4276 15** **** 3216')
])

def test_get_mask_account(cart_number):
    assert get_mask_account('4276155447963216') == '4276 15** **** 3216'
