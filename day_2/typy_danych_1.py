import sys


wiek = 47
rok = 2024
temp = 36.6
print(temp)
print(type(temp))
print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)
print(rok // wiek)
print(5 // 2)
print(rok % wiek)
print(3 % 2)
print(wiek ** rok)
print(f"{wiek ** rok:,}")
wynik = wiek ** rok
print(len(str(wynik)))
print(74 - 8 * 45 + 8 / 2 + 8 / 2)
print(74 - (8 * 45) + 8 / 2 + 8 / 2)
print(74 - (8 * 45) + (8 / 2 + 8) / 2)
print(0.2 + 0.8)
print(0.2 + 0.7)
print(0.1 + 0.2)
print(f"{0.2 + 0.7:.1f}")
print(sys.float_info)
print(f"Sprawdzenie zmiennej temp {temp}, wiek {wiek}")
print(f"""
    {wiek}
    {temp}
""")
print(type(4 / 2))
print(4 / 2)
czy_znasz_pythona = False
print(czy_znasz_pythona)
print(type(czy_znasz_pythona))
print(int(czy_znasz_pythona))
x = 1
print(bool(x))
x = 0
print(bool(x))
x = 100
print(bool(x))
x = -10
print(bool(x))
x = "Karol"
print(bool(x))
x = ""
print(bool(x))
x = None
print(bool(x))
a = 14
b = 3
print(f"wynik porównania {a} > {b} = {a > b}")
print(f"wynik porównania {a} < {b} = {a < b}")
print(f"wynik porównania {a} <= {b} = {a <= b}")
print(f"wynik porównania {a} >= {b} = {a >= b}")
print(f"wynik porównania {a} == {b} = {a == b}")
print(f"wynik porównania {a} != {b} = {a != b}")
print(f"wynik porównania {a > b = }")
print(f"wynik porównania", a, "<", b, "=", a < b)
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(False or True)
print(True or False)
print(False or False)
print(not True)
print(not False)
my_str = '123456789'
print(my_str.isnumeric())
print(my_str.isalnum())
print(my_str.isdecimal())
print(my_str.isalpha())

my_str2 = "12.23"
print(my_str2.isalpha())
print(my_str2.isdecimal())
print(my_str2.islower())
print(my_str2.isalnum())

my_str3 = "0"
print(f"""
    {my_str3.isalnum()}
    {my_str3.islower()}
    {my_str3.isdecimal()}
""")
my_str4 = "Karol123"
print(my_str4.isdecimal())
print(my_str4.isalnum())
print(my_str4.isalpha())
print(my_str4.isupper())
print(my_str4.islower())
print(my_str4.isnumeric())
