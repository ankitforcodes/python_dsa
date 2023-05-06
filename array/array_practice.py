import array

# Create an Array and Traverse through it
my_array = array.array('i', [1,2,3,4,5])

# O(n)
for items in my_array:
	print(items)

# Access individual elements through indexes
print(my_array[2])

# Append any value using append() method
# We can only add one item at a time to the array using append()
# O(1)
my_array.append(10)
print(my_array)

# Insert value in array using insert() method
# O(n)
my_array.insert(0,11)		# 0 is index, 11 is the element that we want to insert
print(my_array)


# Adding more than one element to the array end
# this is called extending an array
new_array = array.array('i', [15,16,17])
my_array.extend(new_array)
print(my_array)


# Remove an element using remove()
# if we try to remove an element that occurs multiple number of time, only first occurence will be deleted
# O(n)
my_array.remove(17)
print(my_array)


# Remove last element using pop()
# O(1)
my_array.pop()
print(my_array)

# Find index of an element
# if we have an element multiple times, the index of first occurence will be returned
# if we try to find index of an element that does not exist, we will get an error
index = my_array.index(2)
print(index)


# Reverse the array using reverse() method
my_array.reverse()
print(my_array)


# Get array's buffer info
# returns two things: the memory address of the 1st element and number of elements in the array
info = my_array.buffer_info()
print(info)


# Check number of occurence of an element in an array
n = my_array.count(10)
print(n)


# Convert array to list
my_list = my_array.tolist()
print(my_list)


# Get range of elements at an index
range_list = my_array[1:5]
print(range_list)
