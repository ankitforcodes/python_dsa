my_dict = {"name": "Ankit", "age":50, "location": "india"}
my_list = [1,2,3,4,5]


# create dictionary from list
my_dict2 = {items:items*2 for items in my_list}
print(my_dict2)


# create ditctionary from dictionary
my_dict3 = {key:value for key,value in my_dict.items()}
print(my_dict3)