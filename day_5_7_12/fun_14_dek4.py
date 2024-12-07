import time
import numpy as np
# pip install numpy
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_wait():
    time.sleep(3)


@measure_time
def my_for_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Sum is:", suma)

@measure_time
def my_sum_without_for():
    total = sum(range(15_000_000))
    print("Sum is:", total)

@measure_time
def my_sum_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print('Sum is:', total)

print("--- Start ---")
my_wait()
my_for_sum()
my_sum_without_for()
my_sum_np()

