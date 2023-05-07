my_list = [1,2,3,4,5]

# M1: 'in' operator
# O(n)
target = 2
if target in my_list:
	print("found")
else:
	print("not found") 

# M2 : traversal
for i in range(len(my_list)):
	if my_list[i] == target:
		print("found at index: ", i)

# when we loop over a list and we need to keep track of both index and element, we use enumerate
for index,value in enumerate(my_list):
	print("Element at index: ", index, "is ", value)