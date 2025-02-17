import pytest

@pytest.fixture
def account_number_fixture():
    return '12345678905555555555'


@pytest.fixture
def cart_number_fixture():
    return '1234567890666666'


@pytest.fixture
def mask_account_cart_fixture():
    return 'Visa Classic 6831982476737658'

@pytest.fixture
def get_date_fixture():
    return '2024-03-11T02:26:18.671407'

# список словарей для src/processing.py/get_filter_by_state
@pytest.fixture
def get_filter_by_state_dict():
    return (
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
         {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'}, # пример без состояния
         {'id': 615064591, 'state': 'Hello', 'date': '2018-10-14T08:21:33.419441'}, # пример неверного состояния
         ])
# ответы для списка словарей при состоянии 'EXECUTED'
@pytest.fixture
def get_filter_by_state_correct_answer():
    return (
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
         ])

# список словарей для src/processing.py/sort_by_date
@pytest.fixture
def list_dict():
    return (
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
         {'id': 615064591, 'state': 'CANCELED' }, # словарь без даты
         {'id': 615064591, 'state': 'Hello', 'date': '17.02.2025 20:15'}, # словарь неверного формата даты
         ])

# список словарей для src/processing.py/sort_by_state
@pytest.fixture
def list_dict_for_sorted_date():
    return ([
         {'id': 615064591, 'state': 'EXECUTED', 'date': '17.02.2025 20:15'}, # словарь с неверным количеством символов
         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019/07/03T18:35:29.4545455'}, # словарь неверного формата
         {'id': 939719571, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, # словари с одинаковыми датами
         {'id': 939719572, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, # словари с одинаковыми датами
         {'id': 939719573, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, # словари с одинаковыми датами
         {'id': 594226727, 'state': 'CANCELED', 'date': '2015-07-07T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2016-06-21T04:21:33.419441'},
         {'id': 615064594, 'state': 'CANCELED', 'date': '2017-05-11T08:21:33.419441'}
        ])

# правильный ответ при заданном False
@pytest.fixture
def correct_answer():
    return ([
        {'id': 594226727, 'state': 'CANCELED', 'date': '2015-07-07T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2016-06-21T04:21:33.419441'},
        {'id': 615064594, 'state': 'CANCELED', 'date': '2017-05-11T08:21:33.419441'},
        {'id': 939719573, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ])

# правильный ответ при заданном True
@pytest.fixture
def correct_answer_true():
    return ([
        {'id': 939719573, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 615064594, 'state': 'CANCELED', 'date': '2017-05-11T08:21:33.419441'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2016-06-21T04:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2015-07-07T21:27:25.241689'}

         ])

@pytest.fixture
def correct_answer_identical():
    return ([
        {'id': 939719571, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 939719572, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 939719573, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        ])




