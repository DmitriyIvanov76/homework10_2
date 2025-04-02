
from src.search_string import search_banking_operation

def test_search_banking_operation(list_bank_operations, answer_search_status):
    assert search_banking_operation(list_bank_operations, 'Открытие вклада') == answer_search_status

def test_absent_status(list_bank_operations):
    assert search_banking_operation(list_bank_operations, 'hello') == []

def test_incorrect_data(list_bank_operations):
    assert search_banking_operation(list_bank_operations, 777) == 'Вы ввели неверные данные!'