import pytest

from nbp_checker import format_date, fetch_exchange_rate

def test_format_date():
    assert format_date("2024-1-2") == "2024-01-02"
    assert format_date("02.01.2024") == "2024-01-02"
    assert format_date("January 2, 2024") == "2024-01-02"


def test_fetch_exchange_rate_valid():
    rate = fetch_exchange_rate("USD", "2024-01-02")
    assert isinstance(rate, float)
    assert rate > 0


def test_fetch_exchange_rate_invalid_date():
    with pytest.raises(ValueError):
        fetch_exchange_rate("USD", "01-01-1700")


def test_fetch_exchange_rate_invalid_currency():
    with pytest.raises(ValueError):
        fetch_exchange_rate("ABC", "06-05-2025")


def test_fetch_exchange_rate_empty_currency():
    with pytest.raises(ValueError):
        fetch_exchange_rate("", "06-05-2025")        
