# Arrays are stored in contigous blocks of memory
# When an element at an index is deleted, that makes the array non-continuous which is not allowed
# So after deleting any element - all elements to the right has to be shifted to keep memory storage continous
# For that reason, deleting last element is very efficent, otherwise its time consuming

import array

my_array = array.array('i', [1,2,3,4,5])
print(my_array)

# Removing element that does not exist will throw an error
# Time Complexity: O(n)
# Space Complexity: O(1)