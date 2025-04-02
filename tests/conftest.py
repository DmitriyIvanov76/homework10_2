import pytest


@pytest.fixture
def account_number_fixture():
    return "12345678905555555555"


@pytest.fixture
def cart_number_fixture():
    return "1234567890666666"


@pytest.fixture
def mask_account_cart_fixture():
    return "Visa Classic 6831982476737658"


@pytest.fixture
def get_date_fixture():
    return "2024-03-11T02:26:18.671407"


# список словарей для src/processing.py/get_filter_by_state
@pytest.fixture
def get_filter_by_state_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},  # пример без состояния
        {"id": 615064591, "state": "Hello", "date": "2018-10-14T08:21:33.419441"},  # пример неверного состояния
    ]


# ответы для списка словарей при состоянии 'EXECUTED'
@pytest.fixture
def get_filter_by_state_correct_answer():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# список словарей для src/processing.py/sort_by_date
@pytest.fixture
def list_dict():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED"},  # словарь без даты
        {"id": 615064591, "state": "Hello", "date": "17.02.2025 20:15"},  # словарь неверного формата даты
    ]


# список словарей для src/processing.py/sort_by_state
@pytest.fixture
def list_dict_for_sorted_date():
    return [
        {"id": 615064591, "state": "EXECUTED", "date": "17.02.2025 20:15"},  # словарь с неверным количеством символов
        {"id": 41428829, "state": "EXECUTED", "date": "2019/07/03T18:35:29.4545455"},  # словарь неверного формата
        {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},  # словари с одинаковыми датами
        {"id": 939719572, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},  # словари с одинаковыми датами
        {"id": 939719573, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},  # словари с одинаковыми датами
        {"id": 594226727, "state": "CANCELED", "date": "2015-07-07T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2016-06-21T04:21:28.419438"},
        {"id": 615064594, "state": "CANCELED", "date": "2017-05-11T08:21:33.419441"},
    ]


# правильный ответ при заданном False
@pytest.fixture
def correct_answer():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2015-07-07T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2016-06-21T04:21:28.419438"},
        {"id": 615064594, "state": "CANCELED", "date": "2017-05-11T08:21:33.419441"},
        {"id": 939719573, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# правильный ответ при заданном True
@pytest.fixture
def correct_answer_true():
    return [
        {"id": 939719573, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064594, "state": "CANCELED", "date": "2017-05-11T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2016-06-21T04:21:28.419438"},
        {"id": 594226727, "state": "CANCELED", "date": "2015-07-07T21:27:25.241689"},
    ]



@pytest.fixture
def correct_answer_identical():
    return [
        {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719572, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719573, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

# для тестирования test_banking_operations и test_search_string
@pytest.fixture
def list_bank_operations():
    return [

            {
                "id": 142264268,
                "state": "CANCELED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                    "name": "USD",
                    "code": "USD"
                  }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
                     },
             {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        {
            "id": 587085106,
            "state": "PENDING",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "from": "Счет 75106830613657914569",
            "to": "Счет 41421565395219882431"
        }
    ]


# для тестирования test_banking_operations
@pytest.fixture
def status_bank_operations():
    return ['Перевод со счета на счет', 'Перевод организации', 'Открытие вклада']

# для тестирования test_search_banking_operation
@pytest.fixture
def answer_search_status():
    return [
        {'id': 587085106, 'state': 'PENDING', 'date': '2018-03-23T10:45:06.972075', 'operationAmount':
        {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
        'description': 'Открытие вклада', 'from': 'Счет 75106830613657914569',
        'to': 'Счет 41421565395219882431'}]

@pytest.fixture
def answer_main():
    return 'Не найдено ни одной транзакции, подходящей под ваши условия фильтрации'




