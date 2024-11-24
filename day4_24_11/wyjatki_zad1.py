# print(5 / 0)
# Traceback (most recent call last):
#   File "/Users/karolkontek/PycharmProjects/bootcamp16_11_2024/day4_24_11/wyjatki_zad1.py", line 2, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
# przechwytywanie i obsługa wyjątków

try:
    # print(5 / 0)
    # print("a" / 2)
    # print(int("A")
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print('Blad typu')
except ValueError:
    print("Blad wartosci")
except Exception as e:
    print("Bład", e)
else:
    print("Wynik", wynik)
finally:
    print("Obliczenia wykonane")
print("Program nadal działa")
