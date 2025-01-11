from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['przykładowa_baza']
kolekcja = db['uzytkownicy']

# kolekcja.insert_one(
#     {'imie':'Jan', 'nazwisko': "Kowalski", 'wiek': 30}
# )
kolekcja.insert_many(
    [
        {'imie':'Anna', 'nazwisko': 'Nowak', 'wiek': 25},
        {'imie':'Paweł', 'nazwisko': 'Wiśniewski', 'wiek': 19},
    ]
)
for uzytkownik in kolekcja.find():
    print(uzytkownik)

print(kolekcja.find_one({"imie": "Jan"}))

client.close()