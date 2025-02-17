def filter_by_state(incoming_data: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """the function returns a list depending on the state"""

    result = list(filter(lambda x: x["state"] in state, incoming_data))
    return result


def sort_by_date(
    incoming_data: list[dict], sorted_parameter: bool = True
) -> list[dict]:
    """function to sort data by date"""
    result = list(
        sorted(incoming_data, key=lambda x: x["date"], reverse=sorted_parameter)
    )
    return result

print(filter_by_state(
    [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
        ))
