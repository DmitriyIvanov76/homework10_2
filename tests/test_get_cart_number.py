from src.masks import get_mask_card_number
from src.generate_cart_namber import generate_number
import pytest

# добавляем в параметризацию функцию генерации номеров карт и их маскировки
@pytest.mark.parametrize('num, res', generate_number(10, 16))

# с помощью параметризации и функции генерации подаем на вход номер карты, проверяем значение на выходе
def test_get_cart_number(num, res):
    assert get_mask_card_number(num) == res

# тестирование с помощью фикстур
def test_get_cart_number_fixture(cart_number_fixture):
    assert get_mask_card_number(cart_number_fixture) == '1234 67** **** 6666'

# вызываем ошибку подавая на вход не верную длину карты
def test_get_mask_number_bad():
    with pytest.raises(ValueError):
        get_mask_card_number('1')

# вызываем ошибку подавая на вход пустое значение
def test_get_cart_number_bad_second():
    with pytest.raises(ValueError):
        get_mask_card_number('')

# вызываем ошибку подавая на вход не числовые символы
def test_get_cart_number_bad_alpha():
    with pytest.raises(ValueError):
        get_mask_card_number('hello')


