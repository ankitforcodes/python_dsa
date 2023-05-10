# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

# pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7)
# Output : ['2+5', '4+3', '3+4', '-2+9']

# O(n*n)
def pair_sum(my_list, num):
	output=[]
	for i in range(len(my_list)):
		for j in range(i+1, len(my_list)):
			if my_list[i] + my_list[j] == num:
				output.append(str(my_list[i]) + '+' + str(my_list[j]))

	return output



print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))