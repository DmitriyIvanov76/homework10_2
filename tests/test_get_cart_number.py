import pytest

from src.generate_cart_namber import generate_number
from src.masks import get_mask_card_number


# добавляем в параметризацию функцию генерации номеров карт и их маскировки
@pytest.mark.parametrize("num, res", generate_number(20, 16))
def test_get_cart_number(num, res):
    assert get_mask_card_number(num) == res


# тестирование с помощью фикстур
def test_get_cart_number_fixture(cart_number_fixture):
    assert get_mask_card_number(cart_number_fixture) == "1234 67** **** 6666"


