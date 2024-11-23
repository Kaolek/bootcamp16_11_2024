tekst = 'Witaj Świecie'
print(tekst)
print(type(tekst))
tekst_upper = tekst.upper()
print(tekst.upper())
print(tekst_upper)
print(tekst)
name = "Karol"
print(len(name))
print(name[0])  #
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[2:4])
print(name[:4])
print(name[:])
str1 = "HELLO WORLD"
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
