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
print(my_str) # " Hello Everyone "
print(my_str.strip()) # "Hello Everyone" - usunięcie spacji i byłych znakó wiodących i kończących
print(my_str.rstrip()) # "  Hello Everyone" - usunięcie po prawej stronie
print(my_str.lstrip()) # "Hello Everyone  " - usunięcie po lewej stronie

my_str2 = '****HELLO****WORLD****'
print(my_str2.strip("*")) # Hello****World
print(my_str2.rstrip("*"))  # ****Hello****World
print(my_str2.lstrip("*")) # Hello****World****

print(my_str) # "  Hello Everyone  "
print(my_str2) # ****HELLO****WORLD****
print(tekst) # Witaj Świecie
             # 0123456789012
print(tekst.removeprefix("Witaj")) # " Świecie"
print(tekst.removesuffix("Świecie")) # "Witaj "
print(tekst.count("i")) # # występuje 3 razy
print(tekst.count("i", 0, 4)) # występuje raz
print(tekst.count("j", 0, 4)) # tylko indeksy 0123, "j" w tym zakresie nie występuje

print(my_str2) # ****HELLO****WORLD****
print(my_str2.replace("HE", "HO")) # ****HOLLO****WORLD****

print(my_str) # "  Hello Everyone  "
print(my_str.replace(" ", "")) # "HelloEveryone"
print(my_str.center(40)) # "             Hello Everyone             ", wycentrowanie tekstu podczas wypisywania

print(tekst.index("Ś")) # indeks numer 6
print(tekst.index("Św")) # indeks numer 6

print("Mój ulubiony serial \"Alternatywy 4\"") # Mój ulubiony serial "Alternatywy 4"
print('Mój ulubiony serial "Alternatywy 4"') # Mój ulubiony serial "Alternatywy 4"
# \ - w stringach tzw znak ucieczki, oznacza nie interpretuj kolejnego znaku tylko po prosty wyświetl

imie = "Karol"
# f-string - sformatowany tekst
formatted_text = f"Mam na imię {imie} i lubie Pythona"
print(formatted_text) # Mam na imię Radek i lubię Pythona - wstrzykiwanie wartości zmiennej do tekstu

formatted_text2 = f"\tMam na imię {imie}\n i lubie Pythona.\b"
print(formatted_text2)
# "	  Mam na imię Radek
#  i lubię pythona"

# starszy sposób wstawiania wartości zmiennej do tekstu
starszy = "Witaj %s!"
print(starszy % imie)  # Witaj Karol!
print("Witaj {}!".format(imie)) # Witaj Karol!

print("""Tekst 
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

# kodowanie znaków np.: utf-8, windows-1250
encoded_s = tekst.encode('utf-8')
print(encoded_s) # b'Witaj \xc5\x9awiecie'
print(type(encoded_s))  # <class 'bytes'>, typ bajtowy
# b - typ bajtowy
# \xc5 - liczba w systemie szesnastkowym -> c5 = 197
print(encoded_s.decode('utf-8')) # "Witaj Świecie"
print(encoded_s.replace(b"j", b"Z")) # b'WitaZ \xc5\x9awiecie'
# encoded_s[4] = b"a" # TypeError: 'bytes' object does not support item assignment
