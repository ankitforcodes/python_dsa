
# O(1)
# Creating empty dictionary
dict1 = dict()

# O(n)
# Creating non-empty dictionary
dict2 = {"name": "Ankit", "age":50}


# Creating dictionary using constructors
dict3 = dict(name="Ankit", age=50)


# Creating dictionary from list of tuples
list_of_tuples = [("name", "Ankit"), ("age", 50)]
dict4 = dict(list_of_tuples)
print(dict4)