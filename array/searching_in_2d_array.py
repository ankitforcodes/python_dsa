import numpy as np


two_d_array = np.array([[1,2,3],[4,5,6],[7,8,9]])

def findElement(array, element):
	for i in range(len(two_d_array)):
		for j in range(len(two_d_array[0])):
			if array[i][j] == element:
				return "found"


	return "not found"

print(findElement(two_d_array, 1))

