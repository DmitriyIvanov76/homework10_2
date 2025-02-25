import pytest

from src.generators import filter_by_currency


# проверка при выборе USD
def test_filter_by_currency_input_usd(correct_filter):
    usd_transactions = filter_by_currency(correct_filter, "USD")
    assert (next(usd_transactions)) == (correct_filter[0])
    assert (next(usd_transactions)) == (correct_filter[1])
    assert (next(usd_transactions)) == (correct_filter[3])


# проверка при выборе RUB
def test_filter_by_currency_input_rub(correct_filter):
    usd_transactions = filter_by_currency(correct_filter, "RUB")
    assert (next(usd_transactions)) == (correct_filter[2])
    assert (next(usd_transactions)) == (correct_filter[4])


# вызов ошибки при вводе неверных данных
def test_filter_by_currency_error(correct_filter):
    with pytest.raises(ValueError):
        next(filter_by_currency(correct_filter, "hello"))
