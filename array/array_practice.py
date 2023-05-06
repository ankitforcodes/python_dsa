import array

# Create an Array and Traverse through it
my_array = array.array('i', [1,2,3,4,5])

# O(n)
for items in my_array:
	print(items)

# Access individual elements through indexes
print(my_array[2])

# Append any value using append() method
my_array.append(10)
print(my_array)