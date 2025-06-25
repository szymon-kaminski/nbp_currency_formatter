import pytest

from formatters.formatter_factory import get_formatter
from formatters.plain import PlainTextFormatter
from formatters.json_fmt import JSONFormatter
from formatters.csv_fmt import CSVFormatter


def test_get_formatter_plain():
    formatter = get_formatter("plain")
    assert isinstance(formatter, PlainTextFormatter)


def test_get_formatter_json():
    formatter = get_formatter("json")
    assert isinstance(formatter, JSONFormatter)


def test_get_formatter_csv():
    formatter = get_formatter("csv")
    assert isinstance(formatter, CSVFormatter)


def test_get_formatter_unknown():
    with pytest.raises(ValueError) as excinfo:
        get_formatter("xml")
    assert "Unknown format type" in str(excinfo.value)


def test_invalid_formatter_type():
    with pytest.raises(ValueError, match="Unknown format type"):
        get_formatter("html")


