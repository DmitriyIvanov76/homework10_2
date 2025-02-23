import random

prime = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "Перевод с карты на карту": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

def filter_by_currency(transactions: list[dict], currency: str) -> iter:
    """функция возвращает итератор, который поочередно выдает транзакции,
     где валюта операции соответствует заданной"""

    # проверка корректности типа входных данных
    if not isinstance(transactions, list) or not isinstance(currency, str):
        raise TypeError('Введено неверное значение')

    # проверка на отсутствие значения ключа 'code'
    for i in transactions:
        if i['operationAmount']['currency']['code'] == '':
            raise ValueError(f'В ID: {i["id"]} отсутствует значение валюта')

    # проверка на наличие выбранной валюты в списке
    for i in transactions:
        if not any(i['operationAmount']['currency']['code'] == currency for i in transactions):
            raise ValueError('Выбранная Вами валюта отсутствует в списке')

    # проводим фильтрацию полученного списка, согласно заданной валюте
    return filter(lambda x: x['operationAmount']['currency']['code'] == currency, transactions)


def transaction_descriptions(transactions: list[dict]) -> iter :
    """функция принимает список словарей с транзакциями
     и возвращает описание каждой операции по очереди"""

    result = (i.get('description', '\033[31mзначение не найдено\033[0m') for i in transactions)
    for i in result:
        yield i

def card_number_generator(start: int, stop: int) -> iter:
    generator_nums = ([0 for i in range(4)] for j in range(4))


for card_number in card_number_generator(1, 5):
    print(card_number)

