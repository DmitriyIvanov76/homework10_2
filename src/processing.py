from datetime import datetime



def filter_by_state(incoming_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """the function returns a list depending on the state"""
    for i in incoming_data:
        if "state" not in i:
            raise ValueError("отсутствует состояние")
    if state not in ["EXECUTED", "CANCELED", "PENDING"]:
        raise TypeError("введено неверное значение состояния")
    result = list(filter(lambda x: x["state"] in state, incoming_data))
    return result


def sort_by_date(incoming_data: list[dict], sorted_parameter: bool = True) -> list[dict]:
    """function to sort data by date"""
    # проверяем формат даты по кол-ву символов
    for i in incoming_data:
        data_str = i.get('date')
        # проверяем соответствует ли дата нужному формату
        try:
            datetime.strptime(data_str, "%Y-%m-%dT%H:%M:%S.%f")
        # в случае не верного формата вызываем ошибку и указываем сбойный id
        except ValueError:
            raise ValueError(f'неверный формат даты в строке с id {i["id"]}')

    # сортируем лист по дате
    result = sorted(incoming_data, key=lambda x: datetime.strptime(x["date"],"%Y-%m-%dT%H:%M:%S.%f"), reverse=sorted_parameter)
    return result

