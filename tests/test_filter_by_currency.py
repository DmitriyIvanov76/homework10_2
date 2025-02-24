import pytest

from src.generators import filter_by_currency



def test_filter_by_currency_input_value(correct_filter):
    usd_transactions = filter_by_currency(correct_filter, "USD")
    assert (next(usd_transactions)) == (correct_filter[0])
    assert (next(usd_transactions)) == (correct_filter[1])
    assert (next(usd_transactions)) == (correct_filter[3])

