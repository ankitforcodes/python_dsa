import numpy as np


two_d_array = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(two_d_array)

# Delete Row 0
new_array = np.delete(two_d_array,0, axis=0)
print(new_array)

# Delete Column 0
newer_array = np.delete(two_d_array,0, axis=1)
print(newer_array)

#TimeComplexity = O(mn)