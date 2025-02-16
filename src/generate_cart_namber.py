import random


def generate_number(count_numb: int, len_num: int) -> list[tuple[str,str]]:
    """функция случайным образом генерирует 16-ти
                значное число"""

    # проверяем, что введены числа
    if not isinstance(count_numb, int) or not isinstance(len_num, int):
        raise TypeError('нужно ввести число')

    # вводим ограничения по кол-ву номеров и кол-ву символов
    if count_numb > 30 or len_num < 12 or len_num > 30 :
        raise ValueError('Вы ввели неверное количество знаков')


    # создаем список в который будут складывать номера карт
    result = []

    # создаем заданное кол-во номеров карт
    for _ in range(count_numb):
        # генерируем случайный номер карты заданной длинны
        number = ''.join([str(random.randint(0, 9)) for _ in range(len_num)])
        # создаем маску под сгенерированный номер карты
        mask = f'{number[0:4]} {number[5:7]}** **** {number[-4:]}'
        # добавляем номера карт
        result.append((number, mask))

    return result







