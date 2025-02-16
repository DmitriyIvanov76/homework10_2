import random

def generate_number(count_numb: int, len_num: int) -> list[str]:
    """функция случайным образом генерирует 16-ти
                значное число"""

    # вводим ограничения по кол-ву номеров и кол-ву символов
    if count_numb > 30 or len_num < 16 or len_num > 30 :
        raise ValueError('Вы ввели неверное количество знаков')

    # проверяем, что введены числа
    if not isinstance(count_numb, int) and not isinstance(len_num, int):
        raise TypeError('нужно ввести число')


    # создаем список в который будут складывать номера карт
    result = []
    # создаем заданное кол-во номеров карт
    for i in range(count_numb):
        # генерируем случайный номер карты заданной длинны
        number = ''.join([str(random.randint(0, 9)) for i in range(len_num)])
        # добавляем номера карт в список
        result.append(number)


    return result

print(generate_number(8, 16))

