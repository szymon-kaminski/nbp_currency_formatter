# NBP Currency Checker

### Description

This is a simple Python CLI tool that fetches currency exchange rates from the National Bank of Poland (NBP) API.  
You can check the exchange rate of a given currency on a specified date. The program also saves the queries to a local file for later reference.

### Features

- Fetches exchange rates for any currency supported by the NBP API.
- Accepts date input in various formats and formats it correctly.
- Handles user input from command line arguments or interactive prompts.
- Saves all queries to a `history.txt` file with currency, rate, and date.
- Clear error messages for invalid inputs or unavailable data.

### Requirements

- Python 3.7+
- `requests` library
- `python-dateutil` library

You can install the dependencies with:

```bash
pip install requests python-dateutil
```

### Usage

Run the program from the command line:

```bash
python main.py [CURRENCY_CODE] [DATE]
```
CURRENCY_CODE: Currency code like USD, EUR, PLN (optional, will prompt if missing)

DATE: Date in any recognizable format (optional, will prompt if missing)

### Example:

```bash
python main.py USD 2025-05-26
```
If arguments are missing, the program will ask for input interactively.

### Output Example

```
Currency Exchange Checker
1 USD = 4.2946 PLN on 2025-05-26
```

### History Logging

Each query is appended to a history.txt file in the project directory, e.g.:

```
1 USD | 4.2946 PLN | 2025-05-26
```

### Running Tests

We use `pytest` to run unit tests.

To run the tests, execute:
```bash
pytest
```
This will run all test cases from ```test_nbp_checker.py.```

### Sample Error Output

If you provide an invalid date or currency, you will get clear feedback:
```
Error: Could not retrieve exchange rate for XXX on 1800-01-01
```

### API Reference

Data is fetched using the official NBP Web API. 
You can explore available endpoints and their formats in the NBP documentation.

### Project Structure

main.py — main script handling user input and output

nbp_checker.py — module with functions to format dates and fetch exchange rates from NBP API

test_nbp_checker.py — unit tests for main functions  

history.txt — log file created at runtime to save query history (not tracked in Git)

.gitignore — to exclude files like __pycache__ and history.txt

### License

This project is open source and free to use.