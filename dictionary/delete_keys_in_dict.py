my_dict = {"name": "Ankit", "age":50, "location": "india"}
print(my_dict)


# O(1)
my_dict.pop('location')
print(my_dict)

# trying to remove a key which is not there will throw error by default
# to prevent error we do:

my_dict.pop('location', None)
print(my_dict)


# Remove all elements using clear()

# O(n)
my_dict.clear()
print(my_dict)