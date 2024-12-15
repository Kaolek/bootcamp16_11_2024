from typing import List

import requests
from pydantic import BaseModel

url = "https://restcountries.com/v3.1/name/Poland"
response = requests.get(url)
print(response)

print(response.text)
data = response.json()
print(type(data))

print(data[0])  # wypisanie pierwszego elementu z listy

country = data[0]
print(f"Nazwa kraju: {country['name']}")

print(f"Nazwa główna: {country['name']['common']}")
print(f"Nazwa oficjalna: {country['name']['official']}")

print(f"Stolica kraju: {country['capital']}")
print(f"Stolica kraju: {country['capital'][0]}")

print(f"Liczba ludności: {country['population']}")


class Pol(BaseModel):
    official: str
    common: str


class NativeName(BaseModel):
    pol: Pol


class Name(BaseModel):
    common: str
    official: str
    nativename: NativeName


class CountryInfo(BaseModel):
    name: Name
    capital: List[str]
    population: int


# country_data = [CountryInfo(**data) for data in response.json()]

# for country in country_data:
    print(country)

print(type(country))
#print(country.name)
