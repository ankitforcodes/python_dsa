#Find pair of numbers in a list whose sum is equal to the number provided

my_list = [1,2,3,3,4,5]
n = 6


for i in range(len(my_list)):
	for j in range(len(my_list)):
		if j>i:
			if my_list[i] + my_list[j] == n:
				print(my_list[i], my_list[j])