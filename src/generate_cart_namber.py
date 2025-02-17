import random


def generate_number(count_numb: int, len_num: int) -> list[tuple[str, str]]:
    """функция случайным образом генерирует 16-ти
    значное число"""

    # проверяем, что введены числа
    if not isinstance(count_numb, int) or not isinstance(len_num, int):
        raise TypeError("нужно ввести число")

    # вводим ограничения по кол-ву номеров и кол-ву символов
    if count_numb > 30 or len_num < 14 or len_num > 30:
        raise ValueError("Вы ввели неверное количество знаков")

    # создаем список в который будут складывать номера карт
    result = []

    # создаем заданное кол-во номеров карт
    for _ in range(count_numb):
        # генерируем случайный номер карты заданной длинны
        number = "".join([str(random.randint(0, 9)) for _ in range(len_num)])
        # создаем маску под сгенерированный номер карты
        mask = f"{number[0:4]} {number[5:7]}** **** {number[-4:]}"
        # добавляем номера карт
        result.append((number, mask))

    return result


def generate_number_account(how_many_account: int, num_account_len: int) -> list[tuple[str, str]]:
    """функция генерирует номер счета и возвращает номер счета и
    последние четыре цифры сгенерированного номера"""

    # проверяем, что введены числа
    if not isinstance(how_many_account, int) or not isinstance(num_account_len, int):
        raise TypeError("нужно ввести число")
    # проверяем введенные данные на количество знаков
    if how_many_account > 30 or num_account_len < 15 or num_account_len > 25:
        raise ValueError("Вы ввели неверное количество знаков")

    # создаем список где будут складываться номера счетов и их замаскированная версия
    account_list = []

    # создаем заданное кол-во номеров
    for _ in range(how_many_account):
        # генерируем номер аккаунта заданной длинны и соединяем все элементы в строку
        number_account = "".join([str(random.randint(0, 9)) for _ in range(num_account_len)])
        # маскируем номер сгенерированного ранее счета
        mask_account = f"**{number_account[-4:]}"
        # складываем полученный результат в список кортежей
        account_list.append((number_account, mask_account))

    return account_list
