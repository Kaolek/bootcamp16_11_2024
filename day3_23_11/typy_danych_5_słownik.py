my_dict = {"A": "one", "B": 'two', 'C': 'three', 'D': 'four'}
print(my_dict)
print(type(my_dict))
empty_dict = dict()
print(empty_dict)
empty_dict2 = {}
print(empty_dict2)
print(type(empty_dict2))
dict_with_integer = {1: 'one', 2: "two", 3: 'three'}
print(dict_with_integer)
dict_mixed = {1: 'one', 'A': "two", 3: 'three'}
print(dict_mixed)
print(dict_mixed.keys())
print(dict_mixed.values())
print(dict_mixed.items())
print(dict_with_integer.keys())
dict_with_list = {1: 'one', 2: 'two', "A": ['asif', 'jhon', 'maria']}
print(dict_with_list)
dict_with_list_and_tuple = {1: 'one', 2: 'two', "A": ['asif', 'jhon', 'maria'], 'B': ('Bat', 'Cat', 'Hat')}
print(dict_with_list_and_tuple)
dict_with_all = {1: 'one',
                 2: 'two',
                 'A': ['asif', 'jhon', 'maria'],
                 "B": ('Bat', 'cat', 'hat'),
                 "C": {"Name", 'age', 10},
                 "D": {"Name", "Radek", "age"}}
print(dict_with_all)
keys = {'a', 'b', 'c', 'd'}
my_dict2 = dict.fromkeys(keys)
print(my_dict2)
value = 10
my_dict3 = dict.fromkeys(keys, value)
print(my_dict3)
value = [10, 20, 30]
my_dict4 = dict.fromkeys(keys, value)
print(my_dict4)
keys = [1, 2, 2, 3, 4, 4, 5]
dict_unique = dict.fromkeys(keys)
print(dict_unique)
list_unique = list(dict_unique)
print(list_unique)
print(list(dict.fromkeys(keys)))
print(my_dict["A"])
print(my_dict["B"])
print(dict_with_integer[1])
print(dict_with_all['D'])
print(dict_with_all['C'])
print(my_dict4.get("a"))
print(my_dict4.get("E"))
print(my_dict4.get("e", "Nie ma"))
my_dict5 = {"Name": "Radek", "ID": 12345, "DDB": 1991, 'Address': "Warsaw"}
print(my_dict5['DDB'])
my_dict5['DDB'] = '1980'
print(my_dict5)
my_dict5['Address'] = "Warsaw Centrum"
print(my_dict5)
dict1 = {"DDB": 1995}
print(dict1)
print(type(dict1))
my_dict5.update(dict1)
print(my_dict5)
my_dict5['Job'] = "Developer"
print(my_dict5)
dict2 = {'cpi': 3.41}
print(dict2)
my_dict5.update(dict2)
print(my_dict5)
print(my_dict5.pop("cpi"))
print(my_dict5)
print(my_dict5.popitem())
print(my_dict5)
del my_dict5['ID']
print(my_dict5)
my_dict5.clear()
print(my_dict5)
del my_dict5
slownik = {'stary_klucz': 'wartosc'}
slownik['nowy_klucz'] = slownik.pop('stary_klucz')
print(slownik)
my_dict5 = {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum', 'Job': 'Developer', 'cpi': 3.41}
my_dict_copy_ref = my_dict5
print(id(my_dict5))
print(id(my_dict_copy_ref))
my_dict_copy = my_dict5.copy()
my_dict5.clear()
print(my_dict_copy)
print(my_dict5)
print(my_dict_copy_ref)
print(f"{id(my_dict5)=}")
print(f"{id(my_dict_copy_ref)=}")
print(f"{id(my_dict_copy)=}")
dict_small = {"x": 3}
dict_small.update([('y', 3), ('z', 7)])
print(dict_small)