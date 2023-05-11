my_dict = {"name": "Ankit", "age":50, "location": "india"}


# copy()
my_dict1 = my_dict.copy()
print(my_dict1)


# get()
name = my_dict.get("name")
title = my_dict.get("title", "Not Found")
print(name)
print(title)


# items()
# create list of tuple as key-value pair
list_of_tuples = my_dict.items()
print(list_of_tuples)


# key()
# returns list of all keys
list_of_keys = my_dict.keys()
print(list_of_keys)


# setdefault()
# sets the provided key if key does not exist
my_dict.setdefault("name", "Sahay")
print(my_dict)
my_dict.setdefault("name1", "Sahay")
print(my_dict)


# pop('key to delete')


# values()
print(my_dict.values())