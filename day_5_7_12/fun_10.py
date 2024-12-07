import operator
from functools import reduce, lru_cache


def add(a, b):
    return a + b


sum_all = reduce(add, [1, 2, 3])
print(f"Reduce [sum_all]: {sum_all}")  # Reduce [sum_all]: 6 ((1+2)+3)

sum_all = reduce(lambda a, b: a + b, [1, 2, 3])
print(f"Reduce [sum_all]: {sum_all}")  # Reduce [sum_all]: 6

product = reduce(lambda a, b: a * b, [1, 2, 3, 4])
print(f"Reduce [product]: {product}")  # Reduce [product]: 24

lista = [1, 2, 3, 45, 67, 78, 100, 200, 300]
sum_all = reduce(lambda a, b: a + b, list(map(lambda n: n * 2, list(filter(lambda n: n % 2 == 0, lista)))))
print("Reduce", sum_all)  # Reduce 1360

l_1 = [i for i in lista if i % 2 == 0]
l_2 = [i * 2 for i in l_1]
sum_all = reduce(lambda a, b: a + b, l_2)
print(sum_all)  # 1360

product = reduce(operator.mul, l_2)
print(f"mul: {product}")  # mul: 29952000000
add = reduce(operator.add, l_2)
print(f"{add}")  # 1360

concat_str = reduce(operator.add, ['Python', 'rocks'])
print(f"Contact: {concat_str}")  # Contact: Pythonrocks

min_num = reduce(lambda a, b: a if a < b else b, l_2)
print(f"Min_numL: {min_num}")  # Min_numL: 4

print(reduce(lambda a, b: bool(a and b), [0, 0, 1, 0, 0]))  # False
print(reduce(lambda a, b: bool(a and b), [0, 0, 0, 0, 0]))  # False
print(reduce(lambda a, b: bool(a or b), [0, 0, 0, 0, 0]))  # False
print(reduce(lambda a, b: bool(a or b), [0, 0, 1, 0, 0]))  # True

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fib = fibonacci(5)
print(fib)  # 5
print(fibonacci.cache_info()) # CacheInfo(hits=3, misses=6, maxsize=1000, currsize=6)
fib = fibonacci(10)
print(fibonacci.cache_info()) # CacheInfo(hits=9, misses=11, maxsize=1000, currsize=11)
print(fib) # 55
# hits - uzyskał wynik bez ponownego
