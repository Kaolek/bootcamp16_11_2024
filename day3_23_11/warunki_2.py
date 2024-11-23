lista = []
lang = input("Podaj znany Ci język programowania")
dane = [1, 2, 3]
match dane:
    case [a, b, c]:
        print(f"Lista z trzema elementami {a=} {b=} {c=}")
