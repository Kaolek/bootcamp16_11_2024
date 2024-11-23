for i in range(10):
    print(i)

for i in range(10):
    print(i, i, sep=":")

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

ludzie = ['radek', 'Janek', "Tomek", "Marek"]
wiek = [45, 40, 18, 23]
for i in range(len(ludzie)):
    print(ludzie[i], wiek[i])