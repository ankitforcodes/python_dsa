# Find if two list are permuation of each other

a = [1,2,3,4,5,1]
b = [1,4,2,3,5,1]


def find_permuation(list1, list2):
	if len(list1) != len(list2):
		return False
	else:
		list1.sort()
		list2.sort()
		if list1 == list2:
			return True
		else:
			return False

print(find_permuation(a,b))