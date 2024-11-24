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

for v in dictionary.values():
    print(v)

for i in dictionary.items():
    print(i)

for k, v in dictionary.items():
    print(k, v, sep=" <=> ")

for k, v in dictionary.items():
    print(k, ":", v)

