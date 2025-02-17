import pytest
from src.widget import get_date

@pytest.mark.parametrize('date_time, res', [
    ('2024-03-11T02:26:18.671407', '11.03.2024'),
    ('2025-03-11T02:26:18.671407', '11.03.2025'),
    ('2019-02-16T02:26:18.671407', '16.02.2019')

])
# проверка функции через параметризацию
def test_get_date(date_time, res):
    assert get_date(date_time) == res

def test_get_date_fixture(get_date_fixture):
    assert  get_date(get_date_fixture) == '11.03.2024'

# вызываем ошибку подавая на вход не числовые символы
def test_get_date_bat_format():
    with pytest.raises(ValueError):
        get_date('gggg-rr-11T02:ee:18.671407')

# вызываем ошибку при вводе пустого значения
def test_get_date_bad_empty():
    with pytest.raises(ValueError):
        get_date('')

# вызываем ошибку при неверной длине пвведенных данных
def test_get_date_bad_len():
    with pytest.raises(ValueError):
        get_date('2024-03-11T02:26:18.6714')

