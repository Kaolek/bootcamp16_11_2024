import xml.etree.ElementTree as ET
import requests
from pydantic import BaseModel
from typing import List

url = "https://api.nbp.pl/api/exchangerates/tables/A/?format=xml"

response = requests.get(url)
print(response)
print(response.text)

xml_data = response.content

root = ET.fromstring(xml_data)
print(root)

table_name = root.find(".//Table").text
print(f"Tabela: {table_name}")

date = root.find(".//EffectiveDate").text
print(f"Tabela: {date}")

no = root.find(".//No").text
print(f"Numer tabeli: {no}")

rates = root.findall(".//Rate")
print(rates)

for rate in rates:
    currency = rate.find("Currency").text
    code = rate.find("Code").text
    mid = rate.find("Mid").text
    print(f"{code} : {currency} - {mid}")


class CurrencyRate(BaseModel):
    currency: str
    code: str
    mid: float


class ExchangeRateTable(BaseModel):
    table: str
    date: str
    number: str
    rates: List[CurrencyRate]


# deserializacja z użyciem Pydantic
currency_rates = []
for rate in rates:
    currency = rate.find("Currency").text
    code = rate.find("Code").text
    mid = rate.find("Mid").text
    currency_rates.append(CurrencyRate(currency=currency, code=code, mid=float(mid)))

exchange_rate_table = ExchangeRateTable(
table=table_name,
    date=date,
    number=no,
    rates=currency_rates
)

print(exchange_rate_table)
rates_pydantic = exchange_rate_table.rates
for rates in rates_pydantic:
    print(rates)