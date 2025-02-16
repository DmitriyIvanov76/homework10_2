
def get_mask_card_number(number_cart: str) -> str:
    """функция принимает на вход номера карты, а возвращает номер с несколькими цифрами закрытыми звездочкой"""

    if len(number_cart) == 16 and number_cart.isdigit():
        return f'{number_cart[0:4]} {number_cart[5:7]}** **** {number_cart[-4:]}'
    else:
        raise ValueError('Ошибка ввода номера карты')


def get_mask_account(number_account: str) -> str:
    """функция принимает на вход номер счета, а возвращает последние четыре цифры счета"""

    if len(number_account) == 20 and number_account.isdigit():
        coded_account_number = "**" + number_account[-4:]
        return coded_account_number
    else:
        raise ValueError('ошибка ввода номера счета')






