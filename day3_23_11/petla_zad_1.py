from itertools import zip_longest

for i in range(10):
    print(i, end="")

print()
print("Koniec pętli")

for i in range(1, 25):
    print(i)

for _ in range(1, 5):
    print("Komunikat")
    print(_)

my_string = "Radek"
for i in my_string:
    print(i)

for i in range(10):
    if i % 2 == 0:
        print(i, "parzysta")

lista3 = [j for j in range(1, 10) if j % 2 == 0]
print(lista3)

for c in lista3:
    if c == 2:
        c += 1
        print("Tylko jeśli c=2")
    print("Przy każdym elemencie pętli", c)

a = 1
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a %= 2
print(a)

imiona = ['Radek', 'Tomek', "Zenek", "Zbyszek"]
for p in imiona:
    print(p)

for i in range(len(imiona)):
    print(i, imiona[1])

for p in imiona:
    print(imiona.index(p), p)

for i in enumerate(imiona):
    print(i)

a, b = (0, 'Radek')
print(a, b)
for pozycja, osoba in enumerate(imiona):
    print(pozycja, imiona)

for p, o in enumerate(imiona, start=1):
    print(p, o)

ludzie = ['radek', 'Janek', "Tomek", "Marek", "Ania"]
wiek = [45, 40, 18, 23]

zipped = zip_longest(ludzie, wiek, fillvalue="NONE")
print(type(zipped))
zipped_tuple = tuple(zipped)
print(zipped_tuple)
for i in zipped:
    print(i)
print("-----------")
for o, w in zipped:
    print(o, w)
print("*" * 25)
for i in zipped_tuple:
    print(i)
for name, age in zipped_tuple:
    print(name, age)

for i in range(0, 10, 2):
    print(i)

for i in range(10, 0, -2):
    print(i)

for i in range(-10, 0, 2):
    print(i)

parzyste = [i for i in range(0, 10, 2)]
print(parzyste)

ang_pol = {'name': 'imię', 'cat': 'kot', 'water': 'woda'}
pol_ang = {}
print(ang_pol.items())
for k, v in ang_pol.items():
    pol_ang[v] = k
print(pol_ang)
print({v: k for k, v in ang_pol.items()})
