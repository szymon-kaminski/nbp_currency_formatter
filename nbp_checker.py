import requests

from dateutil import parser

URL = 'https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/{date}/?format=json'

def format_date(date_str: str) -> str:
    try:
        dayfirst = '.' in date_str or '/' in date_str
        dt = parser.parse(date_str, dayfirst=dayfirst)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        raise ValueError("Wrong date format.")
    

def fetch_exchange_rate(currency: str, date: str, table: str = "A") -> float:
    url = URL.format(table=table, code=currency.lower(), date=date)
    response = requests.get(url)

    if not response.ok:
        raise ValueError("No data for the given currencies or dates.")
    
    data = response.json()
    return data['rates'][0]['mid']


