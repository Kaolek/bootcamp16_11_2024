lista = []
print(lista)
print(type(lista))
print(bool(lista))
pusta_lista = list()
print(pusta_lista)
print(type(pusta_lista))
lista_2 = [10, 20, 30]
print(type(lista_2))
print(lista_2)
lista_3 = [10.77, 30.66, 67, 15]
print(type(lista_3))
print(lista_3)
lista_mieszana = [10, 5.2, "Oko", "Karol"]
print(type(lista_mieszana))
print(lista_mieszana)
print(len(lista_mieszana))
lista.append("Karol")
lista.append("Radek")
lista.append("Tomek")
lista.append("Mateusz")
lista.append("Zbigniew")
print(lista)
print(type(lista))
print(len(lista))
print(lista[1])
print(lista[3])
print(lista[0])
print(lista[len(lista) - 1])
print(lista[-1], lista[4])
print(lista[-2], lista[3])
print(lista[-3], lista[2])
print(lista[-4], lista[1])
print(lista[-5], lista[0])
print(lista[0:3])
print(lista[0:2])
print(lista[:3])
print(lista[:2])
print(lista[-3:])
print(lista[-2:])
print(lista[-1:])
print(lista[-1])
print(lista[-1:][0])
print(lista[-1][0])
print(lista[:])
print(lista[2:4])
print(lista[2:])
print(lista[-3:0])
print(lista[0:-3])
print(lista[2:2])
print(lista[4:10])
print(lista[7:11])
lista[2] = "Mikołaj"
print(lista)
print(len(lista))
lista.insert(1, "Karolina")
print(lista)
print(len(lista))
print(lista.pop(0))
print(lista)
ind = lista.index("Zbigniew")
print("Numer indeksu dla Zbigniew", ind)
print(lista.pop(ind))
print(lista)
print(lista.pop())
lista.append("Radek")
print(lista)
lista.remove("Radek")
print(lista)
print("Mikołaj" in lista)
print("Marta" in lista)
print(lista.remove("Mikołaj"))
print(lista)
lista.append("Mikołaj")
lista.append("Mikołaj")
lista.append("Marcin")
print(lista)
print(lista.index("Mikołaj"))
a = 1
b = 3
a = b
print(f"{a=}")
print(f"{b=}")
b = 7
print(f"{a=}")
print(f"{b=}")
lista_4 = lista
print(f"{lista}")
print(f"{lista_4}")
lista_copy = lista.copy()
lista.clear()
print(f"{lista=}")
print(f"{lista_4=}")
print(f"adres:{id(lista_4)=}")
print(f"adres:{id(lista)=}")
print(f"adres:{id(lista_copy)=}")
liczby = [45, 999, 34, 22, 13.34, 678]
print(liczby)
print(type(liczby))
liczby.sort()
print(liczby)
liczby_a = [45, 999, 22, 13.24, 687, "A"]
print(liczby_a)
print(type(liczby_a))
lista_osoby = ['Radek', 'Ala', 'Agata', 'Lena', 'Justyna']
lista_osoby.sort()
print(lista_osoby)
lista_alfabet = ['a', 'd', 't', 'z']
lista_alfabet.sort()
print(lista_alfabet)
lista_alfabet_pol = ['a', 'z', 'ć', 'g']
lista_alfabet_pol.sort()
print(lista_alfabet_pol)
print(ord("z"))
print(ord("ć"))
lista_osoby.sort(reverse=True)
print(lista_osoby)
lista_osoby.reverse()
print(lista_osoby)
liczby_3 = [3, 8, 5, 12, 1]
liczby_3.reverse()
print(liczby_3)
print(liczby)
print(liczby + liczby_3)
liczby_4 = liczby + liczby_3
print(liczby_4)
liczby_5 = [1, 2, 3, 4, 5]
liczby_6 = [6, 7, 8, 9]
liczby_5.extend(liczby_6)
print(liczby_5)
tekst = "Pth on"
lista_str = list(tekst)
print(lista_str)
lista_str2 = [tekst]
print(lista_str2)
lista_str_pusta = []
lista_str_pusta.append(tekst)
print(lista_str_pusta)
lista_str_pusta = []
lista_str_pusta.extend(tekst)
print(lista_str_pusta)
krotka = tuple(liczby)
print(krotka)
print(type(krotka))
