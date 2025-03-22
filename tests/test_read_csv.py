from unittest.mock import mock_open, patch

from src.read_csv import csv_reader


@patch("builtins.open", new_callable=mock_open, read_data="key,value\nvalue1,value2\n")
def test_read_csv(mock_file):
    result = csv_reader("test.csv")
    assert result == [{"key": "value1", "value": "value2"}]
    mock_file.assert_called_once_with("test.csv", newline="", encoding="UTF-8")
