tupla1 = "Karol"
print(type(tupla1))
tupla2 = ("Karol")
print(type(tupla2))
tupla3 = "karol",
print(tupla3)
tupla4 = ("karol",)
print(type(tupla4))
tupla_name = "Karol", "Zbigniew", "Paweł", "Bartek"
print(type(tupla_name))
print(tupla_name)
temp = 36, 6
print(type(temp))
print(temp)
tupla_liczby = 45, 55, 22.34, 11, 200
tupla_liczby = (45, 55, 22.34, 11, 200)
print(type(tupla_liczby))
print(tupla_liczby)
del temp
print(tupla_liczby)
print(tupla_liczby[:3])
print(tupla_liczby[0:3])
print(tupla_liczby[1:3])
print(tupla_liczby[2:])
print(tupla_liczby[-1])
print(tupla_liczby[::-1])
print(tupla_liczby[-1::-1])
print(tupla_liczby[1:4:2])
print(tupla_liczby[:])
print(tupla_liczby)
print("Radek" in tupla_name)
print(tupla_name.count('Karol'))
print(tupla_name.index("Paweł"))
print(sorted(tupla_name))
print(sorted(tupla_name, reverse=True))
print(tupla_name)
a, b = 1, 2
print(f"{a=} {b=}")
print(type((1, 2)))
a, *b = 1, 2, 3
print(f"{a=} {b=}")
*name1, name2, name3 = tupla_name
print(f"{name1=} {name2=} {name3=}")
name1, *name2, name3 = tupla_name
print(f"{name1=} {name2=} {name3=} ")
tupla_zadanie = "Ola", "Ania", "Ada", "Gabi", "Kasia", "Paulina"
i1, i2, *i3, i4 = tupla_zadanie
print(i1, i2, i3, i4)
print("Jeden", "Dwa", "Trzy")
print("Jeden", "Dwa", "Trzy", sep="")
print("Jeden", "Dwa", "Trzy", sep="=>")
print("Jeden", "Dwa", "Trzy", sep=":")
print("Jeden", "Dwa", "Trzy", sep=":", end="")
print("Dalszy tekst")
print("Karol")
lista = list(tupla_name)
print(lista)
print(type(lista))
print(len(lista))
