import array

my_array = array.array('i', [1,2,3,4,5])

def traverse_array(array):
	for items in array:
		print(items)

traverse_array(my_array)