import datetime
import re
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_cart(user_input: str) -> Union[str, None]:
    """функция маскирует номер карты"""
    # проверка на пустой ввод
    if len(user_input) < 1:
        raise TypeError('вы ничего не ввели')

    # если пользователь ввел карту
    if re.search("[a-zA-Z]", user_input):


        # отделяем тип карты от номера
        type_cart = re.search("[a-z A-Z]+", user_input)
        if type_cart:
            split_type_cart = type_cart.group().strip()
        else:
            raise ValueError('введено неверное значение')

        # отделяем номер карты от типа
        number_cart = re.search(r"\d+", user_input)
        if number_cart:
            split_number_cart = number_cart.group().strip()
        else:
            raise ValueError('введено неверное значение')

        return f"{split_type_cart} {get_mask_card_number(split_number_cart)}"

    # если пользователь ввел счет
    elif re.search("[а-яА-Я]", user_input):

        # отделяем счет от номера
        account_input = re.search("[а-яА-Я]+", user_input)
        if account_input:
            split_account = account_input.group().strip()
        else:
            raise ValueError('введено неверное значение')

        # отделяем номер от счета
        account_number = re.search(r"\d+", user_input)
        if account_number:
            split_account_number = account_number.group().strip()
            return f"{split_account} {get_mask_account(split_account_number)}"
        else:
            raise ValueError('введено неверное значение')

    else:
        return None


def get_date(my_date: str) -> str:
    """функция приводит введенную дату к формату ДД.ММ.ГГГГ"""
    # проверяем на пустое значение
    if len(my_date) != 26:
        raise ValueError('введена неверная дата')
    try:
        date_obj = datetime.datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        raise ValueError('введен неверный формат даты')

    return date_obj.strftime("%d.%m.%Y")

