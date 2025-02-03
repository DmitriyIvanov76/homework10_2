import re
import datetime


def mask_account_card(user_input: str) -> str:
    """функция маскирует номер карты"""

    numbers = re.findall(r"\d+", user_input)
    if not numbers:
        return "please enter correct information"

    card_number = numbers[0]


    card_types = {
        "Classic": "Visa Classic",
        "Platinum": "Visa Platinum",
        "Gold": "Visa Gold",
        "Maestro": "Maestro",
        "Master": "MasterCard",
    }

    for keyword, card_type in card_types.items():
        if re.search(keyword, user_input, re.IGNORECASE):
            return f"{card_type} {card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    if re.search("[а-яА-Я]", user_input):
        return f"Счет **{user_input[-4:]}"




def get_date(my_date: str) -> str:
    """функция приводит введенную дату к формату ДД.ММ.ГГГГ"""
    date_obj = datetime.datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")


print(mask_account_card('Visa Gold 5999414228426353'))