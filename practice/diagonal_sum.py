# Given 2D list calculate the sum of diagonal elements.


myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
# O(n*n)
def diagonal_sum(my_array):
	for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                answer += matrix[i][j]
    return answer


# O(n)
def diagonal_sum1(my_array):
	answer = 0
	for i in range(len(matrix)):
		answer += matrix[i][i]


diagonal_sum(myList2D) # 15