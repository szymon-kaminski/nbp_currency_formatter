from nbp_checker import format_date, fetch_exchange_rate
from formatters.formatter_factory import get_formatter


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


def get_output_format() -> str:
    try:
        return sys.argv[3]
    except IndexError:
        return input("Enter output format (plain / json / csv): ").strip()



def main():
    currency = get_currency()
    user_input_date = get_date()
    output_format = get_output_format()

    formatted_date = safe_format_date(user_input_date)

    try:
        exchange_rate = fetch_exchange_rate(currency, formatted_date)
    except ValueError as e:
        print(e)
        sys.exit(1)

    try:
        formatter = get_formatter(output_format)
    except ValueError as e:
        print(e)
        sys.exit(1)

    data = {currency.upper(): exchange_rate}
    formatted_output = formatter.format(data)

    print("\nCurrency Exchange Checker")
    print(f"Date: {formatted_date}")
    print("Result:")
    print(formatted_output)

    with open("history.txt", "a", encoding="UTF-8") as file:
        file.write(f"{formatted_output} | {formatted_date}\n")


if __name__ == "__main__":
    main()
        
