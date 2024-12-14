from pprint import pprint

# Stworzyć słownik, który ma metode do wyszukiwania najdłuższego klucza w słowniku
class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


# print(len(None)) TypeError: object of type 'NoneType' has no len()


class LongestKeyDictDamian(dict):
    def longest_key(self):
        return max(self.keys(), key=len)


art = LongestKeyDict()
art['tomasz'] = 12
art['abraham'] = 7
art['zen'] = 1
print(art.longest_key()) # abraham

# assert służy do sprawdzania poprawności wyniku
# assert warunek -> komunikat błędu
assert 'abraham' == art.longest_key() # nie ma błędu, jest okey
# assert 'zen' == art.longest_key() # AssertionError
art = LongestKeyDictDamian()
art['tomasz'] = 12
art['abraham'] = 7
art['zen'] = 1
print(art.longest_key())
assert 'abraham' == art.longest_key() # abraham

pprint(art) # {'abraham': 7, 'tomasz': 12, 'zen': 1}

