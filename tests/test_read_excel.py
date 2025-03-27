from unittest.mock import patch

import pandas as pd

from src.read_excel import reader_excel


@patch("pandas.read_excel")
def test_read_excel(mock_read_excel):
    mock_read_excel.return_value = pd.DataFrame({"key": ["value"], "key1": ["value1"]})

    result = reader_excel("test.xlsx")
    assert result == [{"key": "value", "key1": "value1"}]
