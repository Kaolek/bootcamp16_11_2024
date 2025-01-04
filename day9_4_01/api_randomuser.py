from typing import List

import requests
from pydantic import BaseModel

url = "https://randomuser.me/api/"
response = requests.get(url)
print(response) # <Response [200]>
print(response.text)

data = response.json()

user = data['results'][0]
print(user)
print(f"Osoba: {user['name']}")
print(f"Imię: {user['name']['first']}")
print(f"Nazwisko: {user['name']['last']}")

print(f"Numer telefonu: {user['phone']}")

photo_url = user['picture']['large']
print(f"Link do zdjęcia: {photo_url}")

response_photo = requests.get(photo_url)
print(response_photo)
with open("user_photo.jpg", "wb") as f:
    f.write(response_photo.content)
print("Zdjęcie zostało zapisane")

# zbudować schemat klas dla name(first, last), email, picture(large)

class Name(BaseModel):
    title: str
    first: str
    last: str


class Picture(BaseModel):
    large: str


class UserInfo(BaseModel):
    # name: dict
    name: Name
    email: str
    picture: dict

user = data['results'][0]
user_info = UserInfo(**user)
print(user_info)

print(f"Imię: {user_info.name.first}")
print(f"Nazwisko: {user_info.name.last}")
photo_url_pydantic = user_info.picture.large
print(f"Link do zdjęcia: {photo_url_pydantic}")
response_photo_pydantic = requests.get(photo_url_pydantic)
with open("user_photo_pydantic.jpg", "wb") as f:
    f.write(response_photo_pydantic)
print("Zdjęcie zostało zapisane")