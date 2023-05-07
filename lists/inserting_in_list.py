# 4 places to insert
# beginning of list 	O(n)
# end of list 			O(1)
# anywhere in the list
# adding another list to current list


my_list = [1,2,3,4,5]
print(my_list)

# Insert can be used to insert at any index
# first argument is the index at which we want to insert, 2nd argument is the item that we want to insert
my_list.insert(0,6)
print(my_list)


# Inserting element to end of list
my_list.append(7)
print(my_list)


# extend current list by a new list
new_list = [8,9,10]
my_list.extend(new_list)
print(my_list)