my_list= [1,4,2,-2,-9,10,2,12,2,-4,-4,-4,-4,2,6,7] 

peak = my_list[0]
index = 0
output = []

for x in range(1,len(my_list)):
	if (my_list[x]*my_list[x-1] > 0):
		if peak < 0 and my_list[x] < peak:
			peak = my_list[x]
			index = x

		if peak > 0 and my_list[x] > peak:
			peak = my_list[x]
			index = x
	else:
		output.append((index,peak))
		peak = my_list[x]
		index = x

print(output)
