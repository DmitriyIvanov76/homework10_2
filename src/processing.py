from datetime import datetime

def filter_by_state(incoming_data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """the function returns a list depending on the state"""
    for i in incoming_data:
        if 'state' not in i:
            raise ValueError('отсутствует состояние')
    if state not in ['EXECUTED', 'CANCELED']:
        raise TypeError('введено неверное значение состояния')
    result = list(filter(lambda x: x["state"] in state, incoming_data))
    return result


def sort_by_date(
    incoming_data: list[dict], sorted_parameter: bool = True
) -> list[dict]:
    """function to sort data by date"""
    # проверяем формат даты по кол-ву символов(наверное не самый лучший вариант..наверное эта проверка не и нужна..)
    for i in incoming_data:
        if  29 > len(i['date']) >= 20 :
            # проверяем соответствует ли дата нужному формату
            try:
                datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f')
            # в случае не верного формата вызываем ошибку и указываем сбойный id
            except TypeError:
                raise TypeError(f'неверный формат даты в строке с id {i["id"]}')
        else:
            # в случае не верного кол-во символом, вызываем исключение и указываем проблемный id
            raise TypeError(f'неверный формат даты в строке с id {i["id"]}')
    # сортируем лист по дате
    result = list(
        sorted(incoming_data, key=lambda x: x["date"], reverse=sorted_parameter)
    )
    return result

print(sort_by_date([
    {'id': 939719577, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 939719576, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 939719575, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 939719574, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
]), True)

