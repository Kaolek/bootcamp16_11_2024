import chardet

# pip install chardet
with open("test.log", 'r') as file:
    lines = file.read()

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
with open("test.log", "r") as file:
    lines = file.read()

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

file_path = "test.log"
with open(file_path, 'rb') as file:  # rb - odczyt bajtowy
    raw_data = file.read()

print(raw_data)
# b'Powitanie\nKolejne\nJeszcze jedno\nDodane\nDodane\nDodane\nDodane\nDodane\nDo\xc5\x9bdane\nDo\xc5\x9b\xc5\xbc\xc4\x87dane\nDo\xc5\x9b\xc5\x84\xc3\xb3\xc4\x99dane\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}

encoding = result['encoding']
confidence = result['confidence']
print("Kodowanie znaków:", encoding)
print("Trafność:", confidence)

print(raw_data.decode(encoding=encoding))
# Kodowanie znaków: utf-8
# Trafność: 0.99
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