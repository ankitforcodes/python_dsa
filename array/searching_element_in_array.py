import array

my_array = array.array('i', [1,2,3,4,5,6])


def linear_search(array, element):
	for items in array:
		if items == element:
			return "Found"

	return "Not Found"


result = linear_search(my_array, 4)
print(result)

#Time Complexity: O(n)