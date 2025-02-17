import pytest

from src.processing import filter_by_state


# проверка функции по заданному состоянию
@pytest.mark.parametrize(
    "user_data, value, res",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(user_data, value, res):
    assert filter_by_state(user_data, value) == res


# проверка функции по заданному состоянию, значение состояния по умолчанию
def test_filter_by_state_fixture(get_filter_by_state_dict, get_filter_by_state_correct_answer):
    assert filter_by_state(get_filter_by_state_dict[0:4]) == get_filter_by_state_correct_answer


# вызов ошибки при отсутствии параметра 'state'
def test_filter_by_state_error(get_filter_by_state_dict):
    with pytest.raises(ValueError):
        filter_by_state(get_filter_by_state_dict[-2])


# вызов ошибки при неверном параметре 'state'
def test_filter_by_state_error_value(get_filter_by_state_dict):
    with pytest.raises(ValueError):
        filter_by_state(get_filter_by_state_dict[-1])
