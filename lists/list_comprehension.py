# we have a list from which we want to create new list
# logic is: we want to multiple all items of previous list and put in new list

my_list = [1,2,3,4,5]

# M1: Without list comprehension
new_list = []
for items in my_list:
	new_item = items * 2
	new_list.append(new_item)

print(new_list)

# M2: Using list comprehesion

new_list = [item*3 for item in my_list]
print(new_list)


### Conditional List Comprehension ###
my_list = [1,2,3,-5,-7,3,-9,0, -10]
# create new list with only positive numbers

new_list = [item for item in my_list if item > 0]
print(new_list)


### Conditional List Comprehension using funcions
# instead of simple conditions, we use functions

def isEven(num):
	if num%2 == 0:
		return True
	else:
		return False

new_list = [item for item in my_list if isEven(item)]
print(new_list)