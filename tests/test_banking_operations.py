
from src.banking_operations import categorize_operations


def test_banking_operations(list_bank_operations, status_bank_operations):
    assert categorize_operations(list_bank_operations, status_bank_operations) == {
                                                                                   'Перевод со счета на счет': 1,
                                                                                   'Перевод организации': 2,
                                                                                   'Открытие вклада': 1
                                                                                   }

def test_banking_operation_invalid_data(status_bank_operations, list_bank_operations):
    assert categorize_operations(status_bank_operations, list_bank_operations) == 'проверьте входные данные!'
