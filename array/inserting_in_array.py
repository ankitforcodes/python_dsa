import array

my_array = array.array('i',[1,2,3,4,5])
print(my_array)
# Inserting element in the beginning
# We have the provide the index at which we want to insert and then the element 
# 0 -> Index, 6 -> Element
my_array.insert(0,6)
print(my_array)


# Inserting element somewhere in the middle
my_array.insert(3, 9)
print(my_array)


# Inserting element in the end
my_array.insert(7,10)
print(my_array)


# Time complexity: O(n)
# Everytime we insert an element at an index, all the other elements at right hand side index needs to be shifted
# So time-complexity depends on how many elements needs to be shifted
# Worst case scenario - when we add element in the beginning - all the elements of array needs to bw shifted