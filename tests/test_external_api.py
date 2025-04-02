# from unittest.mock import Mock, mock_open, patch
#
# from src.external_api import gen_transaction, sum_transaction
#
#
# @patch("builtins.open", new_callable=mock_open, read_data='[{"ket": "value"}]')
# def test_gen_transaction(mock_file):
#     result = next(gen_transaction())
#     assert result == {"ket": "value"}
#     mock_file.assert_called_once()
#
#
# def test_sum_transaction_rub():
#     """функция тестирования"""
#     mock_code = Mock(
#         return_value={
#             "id": 441945886,
#             "state": "EXECUTED",
#             "date": "2019-08-26T10:50:58.294041",
#             "operationAmount": {"amount": 31957.58, "currency": {"name": "руб.", "code": "RUB"}},
#         }
#     )
#     code = mock_code()
#     assert sum_transaction(code) == 31957.58
#
#
# @patch("requests.get")
#
# def test_sum_transaction_usd(mock_get):
#     """функция для тестирования конвертации в RUB суммы
#     поступившей транзакции с валютой отличной от RUB"""
#
#     mock_dict = Mock(
#         return_value={
#             "id": 41428829,
#             "state": "EXECUTED",
#             "date": "2019-07-03T18:35:29.512364",
#             "operationAmount": {"amount": 8221.37, "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод организации",
#             "from": "MasterCard 7158300734726758",
#             "to": "Счет 35383033474447895560",
#         }
#     )
#     insert_dict = mock_dict()
#     mock_get.return_value.json.return_value = {"result": 85.145342}
#     assert sum_transaction(insert_dict) == 85.145342
