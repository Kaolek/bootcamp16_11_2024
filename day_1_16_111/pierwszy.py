# PEP8 - https://peps.python.org/pep-0008/
# PEP 8 – Style Guide for Python Code
# https://kariera.comarch.pl/blog/clean-code-15-krokow-do-stworzenia-czystego-kodu/
# snake_case - konwencja nazewnicza dla nazw plikó, zmiennych, funkcji
import sys

print()  # wydrukuj/wypisz
# option command l - formatowanie kodu wg zasad PEP8
print("Nazywam się Karol") # Nazywam się Karol
print("Nazywam się Karol") # Nazywam się Karol
print("Nazywam się Karol") # Nazywam się Karol
print("Nazywam się Karol") # Nazywam się Karol
print("Nazywam się Karol") # Nazywam się Karol
# command d - powielenie linii
# print('Nazywam się Karol")
#File "/Users/karolkontek/PycharmProjects/bootcamp16_11_2024/day_1_16_111/pierwszy.py", line 15
#    print('Nazywam się Karol")
#          ^
# SyntaxError: unterminated string literal (detected at line 16)
# Process finished with exit code 1 - program zakończył się z błędem
#  # command / - komentarz zaznaczonych linijek

# type() - sprawdzenie typu danych
print(type("Karol")) # # <class 'str'>, string, dane typu tekstowego

print("39" + "14") # # konkatenacja, łaczenie stringów, 3914

print(39)
print(type(39))  # <class 'int'>, integer - liczby calkowite
# print("39" + 14) # TypeError: can only concatenate str (not "int") to str

print("39" + str(14)) # str() zamiana (rzutowanie) na string, 3914

print(int("39") + 14) # int() - rzutowanie na int, 53

print(5 * "4") # 44444
print(35 * "168")
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
print(35 * 168) # 5880
print(int("35") * int(168)) # 5880

print(sys.int_info)
# sys.int_info(
# bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)
# int w python 64 bitowym ograniczony jest pamięcią

# zmienna - pudełko na dane (przechowywane w pamięci)
# typowanie dynamiczne - typ zmiennej jest określany na podstawie tupu danych jakie do niej wrzucimy
# snake_case - konwencja nazewnicza w pythonie
# camelCase, PascalCase, kebab-case - inne konwencje nazewnicze

# PEP8 mówi, że nazwa powinna podpowiadać co zmienna przechowuje
name = "Karol" # zapisanie danych do zmiennej
print(type(name))  # <class 'str'>
print(name) # wypisanie wartości ze zmiennej
name_info: str = 'Karol' # podpowiedz typu dla programisty
# to nie jest deklaracja typu

# sprawdzmy czy to tylko deklaracja typu
print(name_info) # Karol
print(type(name_info)) # <class 'str'>

name_info = 50
print(name_info) # 50
print(type(name_info)) # <class 'int'>

age = 48
print(age) # 48
print(type(age)) # <class 'int'>
age = "Radek"
# print(age + name_info) # TypeError: can only concatenate str (not "int") to str
age = "48"
print(int(age) + name_info) # 98
