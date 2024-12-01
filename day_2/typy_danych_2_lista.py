# kolekcje
# lista - kolekcja przechowująca dowolną ilość danych dowolnego typu w jenej kolekcji
# mogą byż listy przechowujące mieszane dane (str i int etc...)
# lista zachowuje kolejność przy dodawaniu elementów

lista = []
print(lista) # []
print(type(lista)) # <class 'list'>
print(bool(lista)) # False dla pustej listy

pusta_lista = list()
print(pusta_lista) # []
print(type(pusta_lista)) # <class 'list'>

# deklaracja listy i wypełnienie jej danymi w miejscu deklaracji
lista_2 = [10, 20, 30]
print(type(lista_2)) # <class 'list'>
print(lista_2) # [10, 20, 30]

lista_3 = [10.77, 30.66, 67, 15]
print(type(lista_3)) # <class 'list'>
print(lista_3) # [10.77, 30.66, 67, 15]

# lista mmieszana
lista_mieszana = [10, 5.2, "Oko", "Karol"]
print(type(lista_mieszana)) # <class 'list'>
print(lista_mieszana) # [10, 5.2, 'Oko', 'Radek']

# sprawdzenie ile elemntów znajduje się w kolekcji
print(len(lista_mieszana)) # długosć 4 elementy

# [10, 5.2, 'Oko', 'Radek']
#   0   1     2       3

# dodawanie elementu do listy, na końcu
lista.append("Karol")
lista.append("Radek")
lista.append("Tomek")
lista.append("Mateusz")
lista.append("Zbigniew")
lista.append("Anna")
print(lista) # ['Karol', 'Radek', 'Tomek', 'Mateusz', 'Zbigniew', 'Anna']
print(type(lista)) # <class 'list'>
print(len(lista)) # 6

# ['Karol', 'Radek', 'Tomek', 'Mateusz', 'Zbigniew', 'Anna']
#     0        1        2         3           4          5
#    -6       -5       -4        -3          -2        -1

print(lista[1]) # Radek
print(lista[3]) # Mateusz
print(lista[0]) # Karol

print(lista[len(lista) - 1])  # ostatni element z listy, Anna
print(lista[-1], lista[4]) # Anna Zbigniew
print(lista[-2], lista[3]) # Zbigniew Mateusz
print(lista[-3], lista[2]) # Mateusz Tomek
print(lista[-4], lista[1]) # Tomek Radek
print(lista[-5], lista[0]) # Radek Karol

# print(lista[10]) - lista nie posiada elementu o takim indeksie
# Traceback (most  recent call last):
#   File "C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\day_2_17_11\typy_danych_2_lista.py", line 61, in <module>
#     print(lista[10])
#           ~~~~~^^^^
# IndexError: list index out of range
#
# Process finished with exit code 1

# wypisywanie wielu elementów z listy (slicowanie)
# ['Karol', 'Radek', 'Tomek', 'Mateusz', 'Zbigniew', 'Anna']
#    -6       -5       -4        -3          -2        -1
#     0        1        2         3           4          5
print(lista[0:3]) # ['Karol', 'Radek', 'Tomek']
print(lista[0:2]) # ['Karol', 'Radek']
print(lista[:3]) # ['Karol', 'Radek', 'Tomek']
print(lista[:2]) # ['Karol', 'Radek']
print(lista[-3:]) # ['Mateusz', 'Zbigniew', 'Anna']
print(lista[-2:]) # ['Zbigniew', 'Anna']
print(lista[-1:]) # ['Anna']
print(lista[-1]) # Anna
print(lista[-1:][0]) # Anna
print(lista[-1][0]) # A
print(lista[:]) # ['Karol', 'Radek', 'Tomek', 'Mateusz', 'Zbigniew', 'Anna'] ->012345
print(lista[2:4]) # ['Tomek', 'Mateusz']
print(lista[2:]) # ['Tomek', 'Mateusz', 'Zbigniew', 'Anna']
print(lista[-3:0]) # [] -> [3:0]
print(lista[0:-3]) # [0:3] -> ['Karol', 'Radek', 'Tomek']
print(lista[2:2]) # []
print(lista[4:10]) # ['Zbigniew', 'Anna']
print(lista[7:11]) # []

# nadpisanie elementu w liscie na wskazanym indeksie
lista[2] = "Mikołaj"
print(lista) # ['Karol', 'Radek', 'Mikołaj', 'Mateusz', 'Zbigniew', 'Anna']
print(len(lista)) # długość 6

# rozszerzenie listy, wstawienie elementu na wskazanym indeksie
lista.insert(1, "Karolina")
print(lista) # ['Karol', 'Karolina', 'Radek', 'Mikołaj', 'Mateusz', 'Zbigniew', 'Anna']
print(len(lista))  # długość 7

# usunięcie elemntu z listy
# 1. usunięcie po indeksie -> pop()
# 2. usunięcie po elemencie -> remove()

# po indeksie pop() - zwraca informację co usunął
print(lista.pop(0)) # Karol
print(lista) # ['Karolina', 'Radek', 'Mikołaj', 'Mateusz', 'Zbigniew', 'Anna']
ind = lista.index("Zbigniew") # pierwszy napotkany
print("Numer indeksu dla Zbigniew", ind) # Numer indeksu dla Zbigniew 4
print(lista.pop(ind)) # Zbigniew
print(lista) # ['Karolina', 'Radek', 'Mikołaj', 'Mateusz', 'Anna']
print(lista.pop()) # w liście to usunie ostatni element, Anna

# usunięcie po elemencie, pierwszy napotkany
lista.append("Radek")
print(lista) # ['Karolina', 'Radek', 'Mikołaj', 'Mateusz', 'Radek']
lista.remove("Radek")
print(lista) # ['Karolina', 'Mikołaj', 'Mateusz', 'Radek']

# print(lista.remove("Zenek")) # ValueError: list.remove(x): x not in list, nie ma takiego elementu
print("Mikołaj" in lista) # True
print("Marta" in lista) # False

print(lista.remove("Mikołaj")) # None
print(lista) # ['Karolina', 'Mateusz', 'Radek']
lista.append("Mikołaj")
lista.append("Mikołaj")
lista.append("Marcin")
print(lista) # ['Karolina', 'Mateusz', 'Radek', 'Mikołaj', 'Mikołaj', 'Marcin']
print(lista.index("Mikołaj")) # indeks: 3

a = 1
b = 3
a = b
print(f"{a=}") # a=3
print(f"{b=}") # b=3

b = 7
print(f"{a=}") # a=3
print(f"{b=}") # b=7

lista_4 = lista # a = b, kopiowanie referencji, adres w pamięci
print(f"{lista}")
print(f"{lista_4}")
lista_copy = lista.copy() # kopia elemntów listy do innej listy
# lista = ['Karolina', 'Mikołaj', 'Maciek', 'Marta', 'Marta', 'Marcin']
# lista_4 = ['Karolina', 'Mikołaj', 'Maciek', 'Marta', 'Marta', 'Marcin']

lista.clear() # usunięcie elementów z listy
print(f"{lista=}")
print(f"{lista_4=}")
print(f"{lista_copy=}")
# lista=[]
# lista_4=[]
# lista_copy=['Karolina', 'Mikołaj', 'Maciek', 'Marta', 'Marta', 'Marcin']

# obie listy zostały zmienione
# wskazują na ten sam adres w pamięci
# id() - podaje adres dla danej listy
print(f"adres:{id(lista_4)=}") # adres: id(lista)=1746325475712
print(f"adres:{id(lista)=}") # adres: id(lista_4)=1746325475712
print(f"adres:{id(lista_copy)=}") # adres: id(lista_copy)=1746328345216

liczby = [45, 999, 34, 22, 13.34, 678]
print(liczby) # [45, 999, 34, 22, 13.34, 678]
print(type(liczby)) # <class 'list'>

liczby.sort() # sortowanie
print(liczby) # [13.34, 22, 34, 45, 678, 999]

liczby_a = [45, 999, 22, 13.24, 687, "A"]
print(liczby_a) # [45, 999, 22, 13.24, 687, 'A']
print(type(liczby_a)) # <class 'list'>

lista_osoby = ['Radek', 'Ala', 'Agata', 'Lena', 'Justyna']
lista_osoby.sort()
print(lista_osoby) # ['Agata', 'Ala', 'Justyna', 'Lena', 'Radek']

lista_alfabet = ['a', 'd', 't', 'z']
lista_alfabet.sort()
print(lista_alfabet) # ['a', 'd', 't', 'z']

lista_alfabet_pol = ['a', 'z', 'ć', 'g']
lista_alfabet_pol.sort()
print(lista_alfabet_pol) # ['a', 'g', 'z', 'ć']
print(ord("z")) # 122
print(ord("ć")) # 263

# możemy posortować i odwrócić kolekcję
lista_osoby.sort(reverse=True)
print(lista_osoby) # ['Radek', 'Lena', 'Justyna', 'Ala', 'Agata']

# odwrócenie kolekcji bez sortowania
lista_osoby.reverse()
print(lista_osoby) # ['Agata', 'Ala', 'Justyna', 'Lena', 'Radek']

liczby_3 = [3, 8, 5, 12, 1]
liczby_3.reverse()
print(liczby_3) # [1, 12, 5, 8, 3]

print(liczby)
# nadpisać element czwarty (jaki indeks)
# wypisać ostatni element po indeks dodanich i ujemnych
# zrobić slice(wycinanie) jedno dodatnie, jedno ujemne
# usunąć z listy po indeksie i po elemencie

liczby[3] = 10000  # czwarty element czyli indeks 3
print(liczby[-1])  # wypisanie ostatniego elementu, 999
print(liczby[len(liczby) - 1])  # długosc kolekcji minus 1 wskazuje na ostatni indeks kolekcji
print(liczby[1:3])  # [22, 34]
print(liczby[-2:])  # [687, 999]

liczby.remove(34)  # usunięcie po elemencie(wartości)
print(liczby)  # [13.34, 22, 10000, 687, 999]

print(liczby.pop(2))  # usunięcie po indeksie 2 (to nie jest wartość elementu)
print(liczby)  # [13.34, 22, 687, 999]

# sortowanie i odwrócenie w jednym kroku
liczby.sort(reverse=True)
print(liczby)  # [999, 687, 22, 13.34]

print(liczby[::-1])  # w odwrotnej kolejnoci [13.34, 22, 687, 999]
print(liczby[0:4:2])  # [start:stop:krok] [999, 22]

# łączenie list, dostajemy nową kolekcję
print(liczby + liczby_3)  # [999, 687, 22, 13.34, 1, 12, 5, 8, 3]
liczby_4 = liczby + liczby_3
print(liczby_4)  # [999, 687, 22, 13.34, 1, 12, 5, 8, 3]

liczby_5 = [1, 2, 3, 4, 5]
liczby_6 = [6, 7, 8, 9]
liczby_5.extend(liczby_6)
print(liczby_5)  # zmienia liczby_5, [1, 2, 3, 4, 5, 6, 7, 8, 9]

# rozpakowanie sekwencji
tekst = "Pth on."
lista_str = list(tekst)
print(lista_str)  # ['P', 't', 'h', ' ', 'o', 'n', '.']

lista_str_2 = [tekst]
print(lista_str_2)  # ['Pth on.']

lista_str_pusta = []
lista_str_pusta.append(tekst)
print(lista_str_pusta)  # ['Pth on.']

# rozpakowanie sekwencji, dodanie elemetów kolekcji jako kolejne elementy kolekcji
lista_str_pusta = []
lista_str_pusta.extend(tekst)
print(lista_str_pusta)  # ['P', 't', 'h', ' ', 'o', 'n', '.']

# zamiana listy na krotkę, tuplę
krotka = tuple(liczby)
print(krotka)  # (999, 687, 22, 13.34)
print(type(krotka))  # <class 'tuple'>
