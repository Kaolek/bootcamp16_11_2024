# krotka (tupla) - kolekcja niemutowalna
# lepsze wykorzystanie pamięcią
# jedoelementowa krotka, zmienna, niezmienna - stała

tupla1 = "Karol"
print(type(tupla1)) # <class 'str'>

tupla2 = ("Karol")
print(type(tupla2)) # <class 'str'>

tupla3 = "karol",
print(tupla3) # ('karol',)

# PEP8 sugeruje, by tuplę jednoelementową tworzyć z nawiasami
tupla4 = ("karol",)
print(type(tupla4)) # <class 'tuple'>

tupla_name = "Karol", "Zbigniew", "Paweł", "Bartek"
print(type(tupla_name)) #<class 'tuple'>
print(tupla_name) # ('Karol', 'Zbigniew', 'Paweł', 'Bartek')

temp = 36, 6 # <class 'tuple'>
print(type(temp)) # <class 'tuple'>
print(temp) # (36, 6)

tupla_liczby = 45, 55, 22.34, 11, 200
tupla_liczby = (45, 55, 22.34, 11, 200)
print(type(tupla_liczby)) # <class 'tuple'>
print(tupla_liczby) # (45, 55, 22.34, 11, 200)
# command + strzałka w prawo - przejscie na koniec linii

# tupla jest niemutowalna (imutable) - ni emożna zmienić niz w niej
# temp[0] = 1  # TypeError: 'tuple' object does not support item assignment

# del - usnięcie  z pamięci
# w tupli nie da się usunąć pojedynczego jej elementu
# del temp[0] # TypeError: 'tuple' object doesn't support item deletion

# można usunąc całą tuplę (krotkę)
del temp
# print(temp)  # NameError: name 'temp' is not defined

print(tupla_liczby)
# spróbujcie czy na tupli działa slicowanie
print(tupla_liczby[:3]) # (45, 55, 22.34)
print(tupla_liczby[0:3]) # (45, 55, 22.34)
print(tupla_liczby[1:3]) # (55, 22.34)
print(tupla_liczby[2:]) # (22.34, 11, 200)

print(tupla_liczby[-1]) # 200
print(tupla_liczby[::-1]) # (200, 11, 22.34, 55, 45)
print(tupla_liczby[-1::-1]) # (200, 11, 22.34, 55, 45)
# [start:stop:krok] krok -1 oznacza krok do tyłu
print(tupla_liczby[1:4:1]) # (55, 22.34, 11)
# [-1::-1] -> start=-1, stop=0, krok=-1
print(tupla_liczby[:]) # # [-1::-1]

print(tupla_liczby)
print("Radek" in tupla_name) # False

# count() - zlicza ile razy element występuje w krotce
print(tupla_name.count('Karol')) # 1

# index() - sprawdzenie na którym indeksie znajduje się dany element
print(tupla_name.index("Paweł")) # 2

# sorted() - sortowanie kolekcji
# sortowanie tupli zwraca nową listę posortowaną
print(sorted(tupla_name)) # ['Bartek', 'Karol', 'Paweł', 'Zbigniew']

# sortowanie z odwróceniem
print(sorted(tupla_name, reverse=True)) # ['Zbigniew', 'Paweł', 'Karol', 'Bartek']
print(tupla_name) # ('Karol', 'Zbigniew', 'Paweł', 'Bartek')

# rozpakowanie krotki
a, b = 1, 2 # przypisze do zmiennych wartości wg kolejności
print(f"{a=} {b=}") # a=1 b=2
print(type((1, 2))) # <class 'tuple'>
# a, b = 1, 2, 3 # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3 # * worek na pozostałe dane
print(f"{a=} {b=}") # a=1 b=[2, 3]

#('Karol', 'Zbigniew', 'Paweł', 'Bartek')
# name1, name2, name3
# * moze byc tylko w jednym miejscu
*name1, name2, name3 = tupla_name
print(f"{name1=} {name2=} {name3=}")
#name1=['Karol', 'Zbigniew'] name2='Paweł' name3='Bartek'

name1, *name2, name3 = tupla_name
print(f"{name1=} {name2=} {name3=} ")
#name1='Karol' name2=['Zbigniew', 'Paweł'] name3='Bartek'

name1, name2, *name3 = tupla_name
print(f"{name1=} {name2=} {name3=}")
#name1='Karol' name2='Zbigniew' name3=['Paweł', 'Bartek']

tupla_zadanie = "Ola", "Ania", "Ada", "Gabi", "Kasia", "Paulina"
i1, i2, *i3, i4 = tupla_zadanie
print(i1, i2, i3, i4) # Ola Ania ['Ada', 'Gabi', 'Kasia'] Paulina
"""
    Prints the values to a stream, or to sys.stdout by default.

      sep
        string inserted between values, default a space.
      end
        string appended after the last value, default a newline.
      file
        a file-like object (stream); defaults to the current sys.stdout.
      flush
        whether to forcibly flush the stream.
    """
print("Jeden", "Dwa", "Trzy") # Jeden Dwa Trzy
print("Jeden", "Dwa", "Trzy", sep="") # "" - pusty separator, JedenDwaTrzy
print("Jeden", "Dwa", "Trzy", sep="=>") # "" - pusty separator, Jeden=>Dwa=>Trzy
print("Jeden", "Dwa", "Trzy", sep=":") # "" - Jeden:Dwa:Trzy
print("Jeden", "Dwa", "Trzy", sep=":", end="") # "" - pusty znak konca linii, Jeden:Dwa:Trzy
print("Dalszy tekst") # Jeden:Dwa:TrzyDalszy tekst wypisany bez zmiany do nowej linii
print("Karol") # Karol, w nowej linii bo poprzednia linia ustawiła na domyślny "\n"
# sep: znak oddzielający elelementy (domyślnie " ")
# end: znak na końcu linii (domyślnie "\n" - nowa linia)

lista = list(tupla_name)
print(lista) # ['Karol', 'Zbigniew', 'Paweł', 'Bartek']
print(type(lista)) # <class 'list'>
print(len(lista)) # długość 4
