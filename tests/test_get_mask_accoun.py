import pytest
from src.masks import get_mask_account
from src.generate_cart_namber import generate_number_account

# добавляем в параметризацию функцию генерации счетов и их маскировки
@pytest.mark.parametrize('account_num, res', generate_number_account(20, 20))

# с помощью параметризации и функции генерации подаем на вход номер счета и проверяем значение на выходе
def test_get_mask_account(account_num, res):
    assert get_mask_account(account_num) == res


def test_get_mask_account_fixture(account_number_fixture):
    assert get_mask_account(account_number_fixture) == '**5555'

# вызов ошибки при вводе некорректной длины номера счета
def test_get_mask_account_bad_len():
    with pytest.raises(ValueError):
        get_mask_account('123')

# вызываем ошибку подавая на вход пустое значение
def test_get_mask_account_bad_empty():
    with pytest.raises(ValueError):
        get_mask_account('')



