tekst = 'Witaj Świecie'
print(tekst)  # Witaj Świecie
print(type(tekst))  # <class 'str'>
# teksty są niemutowalne
tekst_upper = tekst.upper()  # """ Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie

name = "Karol"
#       01234 - indeksowanie od zera
print(len(name))  # len() sprawdzanie długości ciągu 5
print(name[0])  # K - pierwsza litera ciągu
print(name[1])  # a
print(name[2])  # r
print(name[3])  # o
print(name[4])  # l
# print(name[5]) # IndexError: string index out of range
# slicowanie
print(name[2:4])  # ro, tylko indeksy 2 i 3 z prawej strony zbiór otwarty
print(name[:4])  # Karo od 0 do 3 (indeks 4 wyłączony)
print(name[:])  # Karol

str1 = "HELLO WORLD"
# str1[0:5] = "HOLAA" #próba zmiany oryginalnego tekstu,
# TypeError: 'str' object does not support item assignment, wynika z tego, że teksty są niemutowalne
print(str1)  # HELLO WORLD

my_str = "  Hello Everyone  "
print(my_str)
print(my_str.strip())
print(my_str.rstrip())
print(my_str.lstrip())
my_str2 = '****HELLO****WORLD****'
print(my_str2.strip("*"))
print(my_str2.rstrip("*"))
print(my_str2.lstrip("*"))
print(my_str)
print(my_str2)
print(tekst)
print(tekst.removeprefix("Witaj"))
print(tekst.removesuffix("Świecie"))
print(tekst.count("i"))
print(my_str2)
print(my_str2.replace("he", "ho"))
print(my_str)
print(tekst.index("Ś"))
print(tekst.index("Św"))
print("Mój ulubiony serial \"Alternatywy 4\"")
print('Mój ulubiony serial "Alternatywy 4"')
imie = "Karol"
formatted_text = f"Mam na imię {imie} i lubie Pythona"
print(formatted_text)
formatted_text2 = f"\tMam na imię {imie}\n i lubie Pythona.\b"
print(formatted_text2)
starszy = "Witaj %s!"
print(starszy % imie)
print("Witaj {}!".format(imie))
print("""Tekst 
    wielolinijkowy""")
encoded_s = tekst.encode('utf-8')
print(encoded_s)
print(type(encoded_s))
print(encoded_s.decode('utf-8'))
print(encoded_s.replace(b"j", b"Z"))
