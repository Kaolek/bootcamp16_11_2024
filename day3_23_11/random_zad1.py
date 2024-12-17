import random
# import - służy do dołączenia do naszego pliku innego pliku, biblioteki, frameworka itd..
# random - działania na liczbach pseudolosowych

print(random.randint(1, 6))  # int od 1 do 6
print(random.randrange(1, 6))  # int od 1 do 5
print(random.randrange(6))  # int od 0 do 5
print(random.random())  # float. 0.25921039232325305 od 0 do 0.9999
print(random.random() * 7)  # float. 1.8798014470462565 od 0 do 6.999

lista = [5, 7, 45, 34, 56]
index = random.randrange(len(lista))  # len() = 5, od 0 do 4
print(index, lista[index])  # 2 45
print(random.choice(lista))  # wylosowany element 34
print("--------------")
print("-" * 20)
# maszyna lotto
# bęben maszyny zawiera kule -> lista
# losowanie kuli -> random
# usunięcie kuli z bębna -> remove
# wyświetlenie w telewizji -> print

lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # losuje z powtórzeniami [9, 44, 19, 20, 27, 15]
print(random.sample(lista_kule, k=6))  # [2, 27, 20, 21, 7, 24] losuje bez powtórzeń
print(random.sample(lista_kule, 6))  # [2, 27, 20, 21, 7, 24] losuje bez powtórzeń
print(random.sample(range(1, 50), 6))  # [18, 17, 48, 41, 47, 11] losuje bez powtórzeń
