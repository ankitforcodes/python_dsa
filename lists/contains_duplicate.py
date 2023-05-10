# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Input: nums = [1,2,3,1]
# Output: true

def find_duplicate(my_list):
	my_set = set(my_list)
	if len(my_set) = len(my_list):
		return True
	else:
		return False

print(find_duplicate([1,2,3,1]))