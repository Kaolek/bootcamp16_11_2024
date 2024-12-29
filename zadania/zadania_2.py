from functools import reduce, lru_cache

# 1
list1 = [[1, 2], [3, 4], [5, 6]]
# proszę o sugestię rozwiązania

# 2
my_list = [1, 2, 3, 3, 6, 7, 3, 8]
element_to_remove = 3
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 6, 7, 8]

# 4
tuple = [(1, 3), (3, 2), (2, 1)]
print(sorted(tuple, key=lambda x: x[1]))
# [(2, 1), (3, 2), (1, 3)]

# 6
imie = "Karol"
print("Mam na {}!!!".format(imie) ) # Mam na Karol!!!

# 8
@lru_cache(1000)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fib = fibonacci(4)
print(fib) # 3

# 9
numbers = [2, 4, 6, 8]
squared = [num ** 2 for num in numbers]
print(f"Squared: {squared}") # Squared: [4, 16, 36, 64]

# 10
name = input("Podaj swoje imię")
surname = input("Podaj swoje nazwisko")
email = ("@wp.pl")
print(f"{name}.{surname}{email}")
