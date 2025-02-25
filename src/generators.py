from typing import Iterator


def filter_by_currency(transactions: list[dict[str]], currency: str) -> Iterator[str]:
    """функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""

    # проверка корректности типа входных данных
    if not isinstance(transactions, list) or not isinstance(currency, str):
        raise ValueError("Введено неверное значение")

    # проверка на отсутствие значения ключа 'code'
    for i in transactions:
        if i["operationAmount"]["currency"]["code"] == "":
            raise ValueError(f'В ID: {i["id"]} отсутствует значение валюта')

    # проверка на наличие выбранной валюты в списке
    for i in transactions:
        if not any(i["operationAmount"]["currency"]["code"] == currency for i in transactions):
            raise ValueError("Выбранная Вами валюта отсутствует в списке")

    # проводим фильтрацию полученного списка, согласно заданной валюте
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)


def transaction_descriptions(transactions: list[dict[str]]) -> Iterator[str]:
    """функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""

    # проверка входных данных
    if not isinstance(transactions, list):
        raise TypeError("Введено неверное значение")
    if not any("description" in i for i in transactions):
        raise KeyError("В списке отсутствует искомое значение")

    # получение нужного значения в словаре и вывод результата
    result = (i.get("description", "\033[31mзначение не найдено\033[0m") for i in transactions)
    for i in result:
        yield i


def card_number_generator(start: int, stop: int) -> iter:
    """Генерирует номера банковских карт согласно заданным значениям"""

    # проверка входных данных
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("введен не верный тип данных")
    if start >= stop:
        raise TypeError("неверное значение")
    # генерация номера карты и вывод согласно формату
    for num in range(start, stop):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:]
