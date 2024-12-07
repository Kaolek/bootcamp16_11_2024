# funkcja zagnieżdżona (funkcja w funkcji)
# wykorzystywane są w dekoratorach

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracanie adresu funkcji


func = fun1()
print(func)  # <function fun1.<locals>.fun2 at 0x102cdcea0>
print(type(func))  # <class 'function'>
func()  # To jest fun2
