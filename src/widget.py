import re

def mask_account_card(user_input: str) -> str:

    numbers = re.findall(r'\d+', user_input)
    if not numbers:
        return 'please enter correct information'

    card_number = numbers[0]

    if re.search('visa', user_input, re.IGNORECASE):
        num_cart_visa = f'Visa Platinum {card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}'
        return num_cart_visa

    elif re.search('maestro', user_input, re.IGNORECASE):
        num_cart_maestro = f'Maestro {card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}'
        return num_cart_maestro

    elif re.search('[а-яА-Я]', user_input):
        num_account = f'Счет **{user_input[-4:]}'
        return num_account

    else:
        error_message = 'please enter correct information'
        return error_message

# Пример использования
print(mask_account_card('Visa Platinum 7000792289606361'))


