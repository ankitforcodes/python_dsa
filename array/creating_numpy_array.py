import numpy as np

# Creating an empty array of integer datatype
my_array = np.array([], dtype=int)						#O(1)

# Creating a non-empty array of integer datatype
my_second_array = np.array([1,2,3,4], dtype=int)		#O(n)
print(my_second_array)