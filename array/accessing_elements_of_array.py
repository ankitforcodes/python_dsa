import array

my_array = array.array('i', [1,2,3,4,5])

def get_element(array, index):
	if index >= len(array):
		print("index out of range")
	else:
		print(array[index])

get_element(my_array,7)


#Time complexity: O(1)