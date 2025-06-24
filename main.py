from nbp_checker import format_date, fetch_exchange_rate

import sys


def get_currency() -> str:
    try:
        return sys.argv[1]
    except IndexError:
        return input("Enter the currency code (e.g. USD, EUR): ").strip()


def get_date() -> str:
    try:
        return sys.argv[2]
    except IndexError:
        return input("Enter the date (e.g. 2025-05-26): ").strip()


def safe_format_date(date_str: str) -> str:
    try:
        return format_date(date_str)
    except ValueError as e:
        print(e)
        sys.exit(1)


def print_result(currency: str, rate: float, date: str) -> None:
    print("\nCurrency Exchange Checker")
    print(f"1 {currency.upper()} = {rate} PLN on {date}")


def save_query_to_file(currency: str, rate: float, date: str) -> float:
    with open("history.txt", "a", encoding="UTF-8") as file:
        file.write(f"1 {currency.upper()} | {rate} PLN | {date}\n")


def main():
    currency = get_currency()
    user_input_date = get_date()
    formatted_date = safe_format_date(user_input_date)

    try:
        exchange_rate = fetch_exchange_rate(currency, formatted_date)
    except ValueError as e:
        print(e)
        sys.exit(1)

    print_result(currency, exchange_rate, formatted_date)

    save_query_to_file(currency, exchange_rate, formatted_date)

if __name__ == "__main__":
    main()
        
