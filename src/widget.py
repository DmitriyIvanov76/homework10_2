import datetime
import re
from typing import Union

from masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> Union[str, None]:
    """функция маскирует номер карты"""
    # если пользователь ввел карту
    if re.search("[a-zA-Z]", user_input):

        # отделяем тип карты от номера
        type_cart = re.search("[a-z A-Z]+", user_input)
        if type_cart:
            split_type_cart = type_cart.group().strip()
        else:
            return None

        # отделяем номер карты от типа
        number_cart = re.search(r"\d+", user_input)
        if number_cart:
            split_number_cart = number_cart.group().strip()
        else:
            return None

        return f"{split_type_cart} {get_mask_card_number(split_number_cart)}"

    # если пользователь ввел счет
    elif re.search("[а-яА-Я]", user_input):

        # отделяем счет от номера
        account_input = re.search("[а-яА-Я]+", user_input)
        if account_input:
            split_account = account_input.group().strip()
        else:
            return None

        # отделяем номер от счета
        account_number = re.search(r"\d+", user_input)
        if account_number:
            split_account_number = account_number.group().strip()
            return f"{split_account} {get_mask_account(split_account_number)}"
        else:
            return None


    return None


print(mask_account_card("Visa Platinum 8990922113665229"))


def get_date(my_date: str) -> str:
    """функция приводит введенную дату к формату ДД.ММ.ГГГГ"""
    date_obj = datetime.datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
