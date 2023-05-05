import array


# Since array can store only homogeneus elements, we have define the datatype of it's element during the time of creation
# As compared to list (which can store heterogeneous elements), arrays are more memory efficient
# because they are stored in contigous memory blocks

# this creates an empty array of type integer('i' denotes integer datatype)
my_array = array.array('i')		#O(1)

# this creates an array of type integers with [1,2,3,4,5] as the elements
another_array = array.array('i', [1,2,3,4,5])		#O(n)