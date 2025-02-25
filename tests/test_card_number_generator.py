import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize(
    "start, stop, result",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (2, 4, ["0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (3, 5, ["0000 0000 0000 0003", "0000 0000 0000 0004"]),
    ],
)
# проверка работы функции
def test_card_number_generator(start, stop, result):
    card_number = card_number_generator(start, stop)
    for answer in result:
        assert next(card_number) == answer


# вызов ошибки если первое значение больше или равно второму
def test_card_number_generator_error(value_error_generate_cart):
    with pytest.raises(TypeError):
        next(card_number_generator(value_error_generate_cart))


# вызов ошибки если введено не цифровое значение
def test_card_number_generator_error_second(value_error_generate_cart_type):
    with pytest.raises(TypeError):
        next(card_number_generator(value_error_generate_cart_type))
