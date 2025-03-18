
from unittest.mock import mock_open, patch

from src.utils import convertor_json


@patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]')
def test_convertor_json(mock_file):
    result = convertor_json("test_path.json")
    assert result == [{"key": "value"}]  # Ожидаем, что result будет равно [{"key": "value"}]
    mock_file.assert_called_once_with("test_path.json", encoding="UTF-8")


def test_convertor_json_error_path():
    error_path = convertor_json("../testpath/test.json")
    assert error_path == []


@patch("builtins.open", new_callable=mock_open, read_data="hello!")
def test_convertor_json_error_file(mock_file):
    error_file = convertor_json("test_path.json")
    assert error_file == []
    mock_file.assert_called_once_with("test_path.json", encoding="UTF-8")
