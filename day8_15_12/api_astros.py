# REST API - sposób komiunikowania się i wymiany danych pomiędzy kleintem a serwerem
# klient np.: przeglądarka
# serwer - tzw. backend, serwer, który ma wystawione metody potrafiące obsłużyć żądania klienta
# GET, POST, PUT/PATCH, DELETE - metody http
# GET - pobiera dane
# POST - do tworzenia obiektu, wysyła dane na serwer, w body można przesłać jsona
# PUT/PATCH - aktualizuje obiekt
# DELETE - usunięcie obiektu
from typing import List

# biblioteka do obsługi metod http
import requests
from pydantic import BaseModel

# pip install requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
print(response)  # <Response [200]>

# statusy http
#
# 2xx - ok
# 3xx - warningi, przekierowania
# 4xx - 404- brak zasobu, 400 Bad Request - błędy parametrów, błędy po stronie klienta
# 5xx - błędy serwera, 500 Internal Server Error

# czysty Json
print(response.text)

# zamiana jsona na słownik
response_data = response.json()
print(type(response_data))  # <class 'dict'>

# wypisać wszystkie klucze ze słownika
for k in response_data:
    print(k)

for k, v in response_data.items():
    print(k, "=>", v)

people_list = response_data['people']
for i in people_list:
    print(i)

# wyświetlić name dla matthew
matthew = response_data['people'][3]['name']
print(matthew)  # Matthew Dominick


class AstroData(BaseModel):
    craft: str
    name: str


class AstroData(BaseModel):
    message: str
    number: int
    people: List[AstroData]


data = AstroData(**response_data)
print(data)

print(data.message)  # success
print(data.number)  # 12

for people in data.people:
    print(people)
    print(people.name)


for p in data.people:
    print(p.__class__.__name__)