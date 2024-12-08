import shutil
from pathlib import Path

base_path = Path('../ops_example')
base_path2 = Path('ops_example/D')

if base_path.exists() and base_path.is_dir():
    """Recursively delate a dictionary tree"""
    shutil.rmtree(base_path)

base_path.mkdir()

path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

# path_b.mkdir()

path_b.mkdir(parents=True)
path_c.mkdir()

for filname in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filname, "w", encoding='utf-8') as stream:
        stream.write(f'Jakaś treść w pliku {filname}')

# przenosi pliki z katalogu B do katalogu D, usunie katalog B
shutil.move(path_b, path_d)  # przenieś
ex1 = path_d / 'ex1.txt'
# zmiana nazwy
ex1.rename(ex1.parent / 'ex1rename.log')

print(base_path.absolute())
# /Users/karolkontek/PycharmProjects/bootcamp16_11_2024/day6_8_12/../ops_example
print(base_path.name)  # nazwa głównego katalogi, ops_example
print(base_path.parent.absolute())
# /Users/karolkontek/PycharmProjects/bootcamp16_11_2024/day6_8_12/..

print(base_path.suffix)
print(ex1.suffix) # .txt
print(base_path.parts) # ('..', 'ops_example')
print(base_path2.parts) # ('ops_example', 'D')
