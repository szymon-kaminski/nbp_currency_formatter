import pytest

from formatters.plain import PlainTextFormatter
from formatters.json_fmt import JSONFormatter
from formatters.csv_fmt import CSVFormatter

data_sample = {"USD": 3.87}


def test_plain_formatter():
    formatter = PlainTextFormatter()
    output = formatter.format(data_sample)
    assert output == "USD: 3.87"


def test_json_formatter():
    formatter = JSONFormatter()
    output = formatter.format(data_sample)
    assert '"USD": 3.87' in output
    assert output.startswith("{")
    assert output.endswith("}")


def test_csv_formatter():
    formatter = CSVFormatter()
    output = formatter.format(data_sample).replace('\r\n', '\n').strip()
    assert output == "Currency,Rate\nUSD,3.87"
