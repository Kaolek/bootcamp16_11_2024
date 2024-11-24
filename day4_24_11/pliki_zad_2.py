import chardet

file_path = "test.log"
with open(file_path, 'rb') as file:
    raw_data = file.read()

print(raw_data)

result = chardet.detect(raw_data)
print(result)
encoding = result['encoding']
confidence = result['confidence']
print("Kodowanie znaków:", encoding)
print("Trafność:", confidence)
print(raw_data.decode(encoding=encoding))
