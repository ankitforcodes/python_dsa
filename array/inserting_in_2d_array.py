import numpy as np


two_d_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_d_array)


# Adding new Column:
# 1 2 3			1 2 3 10
# 4 5 6		=> 	4 5 6 11
# 7 8 9			7 8 9 12

#Arguments => Array in which we are inserting, the index at which we are inserting, the array that we want to insert, inserting is as a row or column
# axis = 1 means we want to insert it as column
new_array = np.insert(two_d_array,2,[[10,11,12]], axis=1)
print(new_array)

# Adding new Row:
# 1 2 3 10
# 4 5 6 11
# 7 8 9 12

newer_array = np.insert(new_array,2,[[13,14,15,16]], axis=0)
print(newer_array)

print(newer_array[0])