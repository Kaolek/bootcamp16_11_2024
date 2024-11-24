licznik = 0
while True:
    print("Komunikat!!!")
    licznik += 1
    if licznik > 15:
        break

print(licznik)
licznik = 0
while licznik < 15:
    licznik += 1
    print("Komunikat 2 !!!!")

# password = input("Podaj hasło")
# while password != 'secret':
#     password = input("Błędne hasło. Podaj hasło")
# print("Hasło prawidłowe")
#
# ista = []
# ista_int = []
# hile True:
#   wej = input("Podaj liczbę")
#   if not wej.isnumric():
#       break
#   lista.append(wej)
#   lista_int.append(int(wej))
#
# rint(lista)
# rint(lista_int)
my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)
print(my_list)
