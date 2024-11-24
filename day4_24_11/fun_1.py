# funkcje - wydzielony fragment programu wykonac w dowolnym momencie
# funkcja przed użyciem musi zostać zdefiniowana
# w miejscu definicji funkcja sie nie wykonuje
# aby funkcja sie uruchmiła musimy ją wywołac
# zmienne globalne
# widoczne również wewątrz funkcji
a = 6
b = 8


# PEP8 zaleca by definicja funkcji była oddzielona od reszty programu dwoma pustymi linijkami
# deinicjia funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):
    print(a + b)


def odejmij(a, b, c=0):
    print(a - b - c)


# wywołanie funkcji
# nazwa funkcji i nawiasy ()
print(dodaj)  # wypisze adres funkcji dodaj
print(type(dodaj))  # <class 'function'> funkcja
dodaj()  # uruchomienie funkcji, 14
dodaj2(10, 67)  # 77
odejmij(1, 2)  # c=0, -1
odejmij(1, 2, 3)  # c=3, -4

## argumenty przekazane po nazwie
odejmij(c=9, a=9, b=88)  # -88
odejmij(b=67, a=78)  # 11
dodaj2(b=7, a=9)

# mieszane
odejmij(1, c=90, b=87)
odejmij(1, b=87)
dodaj2(3, b=89)

# nie można przekazywać argumentów pozycyjnych po nazwanych
# odejmij (c=90, 3, 4) #

print("-----------")
print(dodaj())

# print(dodaj() + dodaj()) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# jeli funkcja nie zwraca wyniku nie możemy tego wyniku dalej użyć