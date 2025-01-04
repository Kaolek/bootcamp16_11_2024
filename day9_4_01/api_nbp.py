import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"
response = requests.get(url)
print(response)
print(response.text)

table = response.json()
print(table)
print(type(table))
print(f"Waluta: {table['currency']}")
print(f"Rates: {table['rates']}")
print(f"Kurs {table['currency']} wynosi {table['rates'][0]['mid']} pln")