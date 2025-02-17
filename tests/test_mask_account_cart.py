import pytest

from src.widget import mask_account_cart


# добавляем параметризацию
@pytest.mark.parametrize(
    "type_num_cart, res",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 92** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 37** **** 5199"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 14** **** 6353"),
        ("MasterCard 7158300734726758", "MasterCard 7158 00** **** 6758"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_account_cart(type_num_cart, res):
    assert mask_account_cart(type_num_cart) == res


# проверяем функцию через фикстуру
def test_account_cart_fixture(mask_account_cart_fixture):
    assert mask_account_cart(mask_account_cart_fixture) == "Visa Classic 6831 82** **** 7658"


# вызов ошибки при вводе неверного значения
def test_account_cart_bad_incorrect_value():
    with pytest.raises(ValueError):
        mask_account_cart("hello")


# вызов ошибки при вводе неполного номера карты
def test_account_cart_bad_low_len():
    with pytest.raises(ValueError):
        mask_account_cart("Maestro 159")


# вызов ошибки при вводе пустого значения
def test_account_cart_bad_empty():
    with pytest.raises(TypeError):
        mask_account_cart("")


# вызов ошибки при вводе русских символов
def test_account_cart_bad_cyrillic():
    with pytest.raises(ValueError):
        mask_account_cart("привет")
