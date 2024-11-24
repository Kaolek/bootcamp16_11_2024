# praca z plikami
# t = open("nazwa_pliku", "parametr")
# context manager
# with
# to pozwala na bezpieczną pracę z plikami
from webbrowser import open_new

with open("test.log", "w") as fh:  # filehandler
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

with open("../test.log", "w") as fh:
    fh.write("Powitanie\n")

with open("../test.log", "w") as fh:
    fh.write("Nadpisane\n")

# with open("../test.log", "x") as fh:
#     fh.write("Powitanie\n")
# Traceback (most recent call last):
#   File "/Users/karolkontek/PycharmProjects/bootcamp16_11_2024/day4_24_11/pliki_zad_1.py", line 19, in <module>
#     with open("../test.log", "x") as fh:
#          ^^^^^^^^^^^^^^^^^^^^^^^^
# FileExistsError: [Errno 17] File exists: '../test.log'

with open("test.log", "a") as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dośdane\n")
with open("test.log", "r") as f:
    lines = f.read()
print(lines)