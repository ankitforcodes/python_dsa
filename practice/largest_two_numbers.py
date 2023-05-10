# Given a list, write a function to get first, second best scores from the list

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

#first_second(myList) # 90 87

def first_second(myList):
	max1 = float('-inf')
	max2 = float('-inf')

	for num in myList:
		if num > max1:
			max1 = num
			max2 = max1
		elif num > max2:
			max2 = num