import pytest

from src.generators import transaction_descriptions


# проверка работы функции
def test_transaction_descriptions(correct_filter):
    descriptions = transaction_descriptions(correct_filter)
    assert next(descriptions) == correct_filter[0]["description"]
    assert next(descriptions) == correct_filter[1]["description"]
    assert next(descriptions) == correct_filter[2]["description"]
    assert next(descriptions) == correct_filter[3]["description"]


# вызов ошибки при отсутствии описания
def test_transaction_descriptions_error(correct_filter):
    with pytest.raises(KeyError):
        descriptions = transaction_descriptions(correct_filter[5:])
        print(next(descriptions))
