user = "Karol"  # str
wiek = 39  # int
wersja = 3.90001  # <class 'float'> liczby zmiennoprzecinkowe
print(type(wersja))  # <class 'float'>
liczba = 567980123456  # int (Python nie ma czegos w rodzaju bigint, double, longint etc...)

print("Witaj %s masz teraz %d lat" % (user, wiek))  # Witaj Karol masz teraz 39 lat
# Przy takim wypisywaniu sprawdza typy danych
# print("Witaj %d masz teraz %s lat" % (user, wiek))#TypeError: %d format: a real number is required, not str

print("Witaj %(user)s, masz teraz %(wiek)d lat" % {'user': user, "wiek": wiek})
# Witaj Karol, masz teraz 39 lat
# print("Witaj %d masz teraz %s lat" % (user, wiek))#TypeError: %d format: a real number is required, not str
# shift command strałka w dól - przesunięcie wiersza

print("Witaj %(user)s, masz teraz %(wiek)d lat, miło Cię widzieć %(user)s" % {'user': user, "wiek": wiek})
# Witaj Karol, masz teraz 39 lat, miło Cię widzieć Karol

# zrobic taki tekst uzywając f-string f"{}"
# tu nie sprawdza typów
print(f"Witaj {user}, masz teraz {wiek} lat. Miło Cię widzieć {user}")
# Witaj Karol, masz teraz 39 lat. Miło Cię widzieć Karol

print("Witaj {}, masz teraz {} lat".format(user, wiek))
# Witaj Karol, masz teraz 39 lat

print('Używamy wersjiu Pythona %i' % 3)  # Uzywamy wersji Pythona 3
print('Używamy wersjiu Pythona %f' % 3.9)  # Uzywamy wersji Pythona 3.900000
print('Używamy wersjiu Pythona %.1f' % 3.9)  # Uzywamy wersji Pythona 3.9 .1f - jedno miejsce po przecinku
print('Używamy wersjiu Pythona %.2f' % 3.9)  # Uzywamy wersji Pythona 3.90
print('Używamy wersjiu Pythona %.0f' % 3.9)  # Używamy wersji Pythona 4 - zaokrąglił, 0 miejsc po przecinku
print('Używamy wersjiu Pythona %.f' % 3.9)  # Używamy wersji Pythona 4 - zaokrąglił, 0 miejsc po przecinku

x = 3.99
print("Liczba %.f" % x)  # Liczba 4, zaokrąglona do wypisania
print("Liczba się nie zmieniła", x)  # Liczba się nie zmieniła 3.99

# zaokrąglenie matematyczne
x = round(x)
print("Liczba po zaokrągleniu", x) # Liczba po zaokrągleniu 4

x = 3.14157890
x = round(x, 2)
print("Liczba zaokrąglona do dwóch miejsc", x) # Liczba zaokrąglona do dwóch miejsc 3.14

print("Używamy wersji pythona {}".format(wersja))
# Używamy wersji pythona 3.90001

print(f"Używamy wersji pythona {wersja}") # Używamy wersji pythona 3.90001
print(f"Używamy wersji pythona {wersja:.1f}") # Używamy wersji pythona 3.9
print(f"Używamy wersji pythona {wersja:.2f}") # Używamy wersji pythona 3.90
print(f"Używamy wersji pythona {wersja:.0f}") # Używamy wersji pythona 4
# również zaokrągli,
# dla 0 miejsc po przecinku w tym przypadku musimy podać jawnie .0f

print(liczba) # 56798123456

print("Nasza duża liczba {}".format(liczba)) # 567980123456
print("Nasza duża liczba {:,}".format(liczba)) # Nasza duża liczba 560,798,123,456
# :, - oznacza oddziel sekcje po 3 przecinkami
print(f"Nasz duża liczba {liczba:,}")
# Nasz duża liczba 567,980,123,456

# zamienić , na spacje
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))
# Nasza duża liczba 567 980 123 456
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))
# Nasza duża liczba 567.980.123.456

liczba_human_readable = f'Nasza duża liczba {liczba:_}'
print(liczba_human_readable) # Nasza duża liczba 567_980_123_456

# parametr = 150000000000
parametr = 150_000_000_000 # pomoc dla programisty, czytelniejszy zapis
print(parametr)  # 150000000000
print(type(parametr)) # <class 'int'>

print(f"{user:>10}") # "     Tomek" - wyrównał do prawej do długości 10 znaków
print(f"{user:<15}") # "Tomek          " - wyrównał do lewej
print(f"{user:^20}")  # "       Tomek        " - wyśrodkowane

tekst = "jeden dwa trzy cztery"
# Podzielenie tekstu po znaku " "
print(tekst.split()) # ['jeden', 'dwa', 'trzy', 'cztery']
tekst2 = "jeden, dwa, trzy, cztery"
print(tekst2.split(",")) # ['jeden', ' dwa', ' trzy', ' cztery']
print(tekst2.split(", ")) # ['jeden', 'dwa', 'trzy', 'cztery']
