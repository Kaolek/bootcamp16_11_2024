import requests
from pydantic import BaseModel
from typing import List
from datetime import date
url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"
url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"
response = requests.get(url)
print(response)
print(response.text)

table = response.json()
print(table)
print(type(table))
print(f"Waluta: {table['currency']}")
print(f"Rates: {table['rates']}")
print(f"Kurs {table['currency']} wynosi {table['rates'][0]['mid']} pln")


# zbudować model klas
# deserializacja na obiekty

class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class CurrencyData(BaseModel):
    table: str
    currency: str
    code: str
    rates: List[Rate]


currency_data = CurrencyData(**table)
print(currency_data)

print(currency_data.currency)
print(currency_data.code)
print(currency_data.rates[0].mid)
print(currency_data.rates[0].effectiveDate)