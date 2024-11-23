user = "Karol"
wiek = 39
wersja = 3.90001
print(type(wersja))
liczba = 56798123456
print("Witaj %s masz teraz %d lat" % (user, wiek))
print("Witaj %(user)s, masz teraz %(wiek)d lat" % {'user': user, "wiek": wiek})
print("Witaj %(user)s, masz teraz %(wiek)d lat, miło Cię widzieć %(user)s" % {'user': user, "wiek": wiek})
print(f"Witaj {user}, masz teraz {wiek} lat. Miło Cię widzieć {user}")
print("Witaj {}, masz teraz {} lat".format(user, wiek))
print('Używamy wersjiu Pythona %i' % 3)
print('Używamy wersjiu Pythona %f' % 3.9)
print('Używamy wersjiu Pythona %.1f' % 3.9)
print('Używamy wersjiu Pythona %.2f' % 3.9)
print('Używamy wersjiu Pythona %.0f' % 3.9)
print('Używamy wersjiu Pythona %.f' % 3.9)
x = 3.99
print("Liczba %.f" % x)
print("Liczba się nie zmieniła", x)
x = 3.14157890
x = round(x, 2)
print("Liczba zaokrąglona do dwóch miejsc", x)
print("Używamy wersji pythona {}".format(wersja))
print(f"Używamy wersji pythona {wersja:.1f}")
print(f"Używamy wersji pythona {wersja:.2f}")
print(f"Używamy wersji pythona {wersja:.0f}")
print(liczba)
print("Nasza duża liczba {}".format(liczba))
print("Nasza duża liczba {:,}".format(liczba))
print(f"Nasza duża liczba {liczba:,}".replace(",", ""))
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))
liczba_human_readable = f'Nasza duża liczba {liczba:_}'
print(liczba_human_readable)
parametr = 150_000_000_000
print(parametr)
print(type(parametr))
print(f"{user:>10}")
print(f"{user:<15}")
print(f"{user:^20}")
tekst = "jeden dwa trzy cztery"
print(tekst.split())
tekst2 = "jeden, dwa, trzy, cztery"
print(tekst2.split(","))
print(tekst2.split(", "))