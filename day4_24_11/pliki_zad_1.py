# praca z plikami
# t = open("nazwa_pliku", "parametr")
# context manager
# with
# to pozwala na bezpieczną pracę z plikami
#  ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================

with open("test.log", "w") as fh:  # filehandler
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

with open("../test.log", "w") as fh:  # # filehandler, ten plik bedzie w nadrzędnym katalogu
    fh.write("Powitanie\n")

# w - kasuje plik jesli istnieje
with open("../test.log", "w") as fh:  # filehandler, ten plik bedzie w nadrzędnym katalogu
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
    file.write("Dośżćdane\n")
    file.write("Dośńóędane\n")
with open("test.log", "r") as f:
    lines = f.read()
print(lines)
# Powitanie
# Kolejne
# Jeszcze jedno
# Dodane
# Dodane
# Dodane
# Dodane
# Dodane
# Dośdane
# Dośżćdane
# Dośńóędane