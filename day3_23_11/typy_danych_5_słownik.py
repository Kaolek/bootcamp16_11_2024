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
