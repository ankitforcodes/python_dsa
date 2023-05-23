my_list = [5,2,3,4,1,6,7,5,9,0]

def bubble_sort(my_list):
	sorted_flag = False
	while not sorted_flag:
		sorted_flag = True
		for i in range(len(my_list)-1):	#-1 because we wont be comparing the last element with any next element
			if my_list[i] > my_list[i+1]:
				my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
				sorted_flag = False
	return my_list


print(bubble_sort(my_list))