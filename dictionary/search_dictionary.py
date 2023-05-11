my_dict = {"name": "Ankit", "age":50, "location": "india"}

search_for = "india1"

for keys in my_dict:
	if my_dict[keys] == search_for:
		print(keys, my_dict[keys])
