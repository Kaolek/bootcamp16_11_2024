lista = ["Ananas", "Cytryna", "Jagody", "Kiwi", "Banan"]
print(type(lista))  # <class 'list'>
print(lista)  # ['Ananas', 'Cytryna', 'Jagody', 'Kiwi', 'Banan']

print(len(lista))  # 5
# ['Ananas', 'Cytryna', 'Jagody', 'Kiwi', 'Banan']
#     0          1         2         3       4

print(lista[1])  # Cytryna

lista[2] = "Malina"
print(lista)
# ['Ananas', 'Cytryna', 'Malina', 'Kiwi', 'Banan']

tupla = "Niebieski", "Zielony", "Czerwony"
print(type(tupla))  # <class 'tuple'>
print(tupla)  # ('Niebieski', 'Zielony', 'Czerwony')
print(tupla[-1])  # Czerwony

nazwa = "Karol Kontek"
print(type(nazwa))  # <class 'str'>
print(nazwa)  # Karol Kontek
nazwa_2 = nazwa.split()
print(nazwa_2)  # ['Karol', 'Kontek']
imie = nazwa_2[0]
print(imie)  # Karol
nazwisko = nazwa_2[1]
print(nazwisko)  # Kontek

imie_2 = "Jan"
wiek = 25
print(f"Mam na imię {imie_2} i mam {wiek} lat")
# Mam na imię Jan i mam 25 lat

lista_2 = [1, 2, 3, 4, 5]
print(type(lista_2))  # <class 'list'>
print(len((lista_2)))  # 5

lista_3 = [1, 2, 3]
lista_4 = [4, 5, 6]
print(lista_3 + lista_4)  # [1, 2, 3, 4, 5, 6]
lista_5 = lista_3 + lista_4
print(lista_5)  # [1, 2, 3, 4, 5, 6]

lista_6 = [1, 2, 3]
lista_6.append(4)
print(lista_6)  # [1, 2, 3, 4]

tupla_2 = 1, 2, 3, 4, 5
print(type(tupla_2))  # <class 'tuple'>
print(tupla_2)  # (1, 2, 3, 4, 5)
print(tupla_2[2])  # 3

lista_7 = [1, 2, 3, 4, 5]
lista_7.reverse()
print(lista_7)  # [5, 4, 3, 2, 1]
maks_element = max(lista_7)
print(maks_element)  # 5

nazwa_3 = "Python"
nazwa_4 = "jest super"
nazwa_5 = (nazwa_3 + " " + nazwa_4)
print(nazwa_5)  # Python jest super

nazwa_6 = "Lubię Pythona"
nazwa_7 = nazwa_6.replace("Pythona", "programowanie")
print(nazwa_7)  # Lubię programowanie

tekst_2 = "Lubię Pythona"
tekst_3 = tekst_2.split()[1]
print(tekst_3)  # Pythona

lista_8 = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(len(lista_8)) # 9
print(lista_8[:5]) # [2, 4, 6, 8, 10]