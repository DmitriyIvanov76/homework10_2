from datetime import datetime


def filter_by_state(incoming_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """the function returns a list depending on the state"""
    for i in incoming_data:
        if "state" not in i:
            raise ValueError("отсутствует состояние")
    if state not in ["EXECUTED", "CANCELED"]:
        raise TypeError("введено неверное значение состояния")
    result = list(filter(lambda x: x["state"] in state, incoming_data))
    return result


def sort_by_date(incoming_data: list[dict], sorted_parameter: bool = True) -> list[dict]:
    """function to sort data by date"""
    # проверяем формат даты по кол-ву символов(наверное не самый лучший вариант..наверное эта проверка не и нужна..)
    for i in incoming_data:

        # проверяем соответствует ли дата нужному формату
        try:
            datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f")
        # в случае не верного формата вызываем ошибку и указываем сбойный id
        except ValueError:
            raise ValueError(f'неверный формат даты в строке с id {i["id"]}')

    # сортируем лист по дате
    result = list(sorted(incoming_data, key=lambda x: x["date"], reverse=sorted_parameter))
    return result
