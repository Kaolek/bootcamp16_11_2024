dictionary = {'imię': "Radek", 'nazwisko': "Kowalski"}
print(dictionary)  # {'imię': 'Radek', 'nazwisko': 'Kowalski'}
print(type(dictionary))  # <class 'dict'>

# wypisanie kluczy
for k in dictionary:
    print(k)
# imię
# nazwisko

for k in dictionary.keys():
    print(k)
# imię
# nazwisko

# wypisanie wartości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wypisanie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, v, sep=" <=> ")
# imie <=> Radek
# nazwisko <=> Kowalski

for k, v in dictionary.items():
    print(k, ":", v)
# imie : Radek
# nazwisko : Kowalski