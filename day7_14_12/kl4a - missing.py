# __missing__ - metoda wykonywana gdy nie ma klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


d_python = {}
print(type(d_python))  # <class 'dict'>
print(d_python)  # {}
# print(d_python['name'])  KeyError: 'name'
d_python['name'] = "Radek"
print(d_python['name'])  # Radek

d1 = DefaultDict()
print(d1['name'])  # default - nadpisaliśmy metodę __missing__


class Autodict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


d2 = Autodict()
print(d2)
print(d2['name'])
print(d2)
print(d2['name'])
d2['name'] = "Radek"
print(d2['name'])

# słownik, gdzie klucze są zapamiętane małą literą
# zwrócimy wartość dla klucza niezależnie od wielkości liter

# print(1.lower()) SyntaxError: invalid decimal literal
# print(2.casefold()) SyntaxError: invalid decimal literal
class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return self.get(key.casefold())

d3 = CaseInsensitiveDict()
d3['name'] = "Radek"
print(d3["NaMe"])
d3[1] = "Tomek"
print(d3)
print(d3[1])
# class CaseInsensitiveDict():
#     def __missing__(self, key):
