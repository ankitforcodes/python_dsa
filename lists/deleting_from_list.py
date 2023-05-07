my_list = [1,2,3,4,5]
print(my_list)
# delete element using pop()
# pop(2) will remove element present at index 2
# O(n)
my_list.pop(2)
print(my_list)

# removing element using del()
del my_list[0]
print(my_list)
del my_list[0:2]
print(my_list)


# deleting element directly without index
my_list.remove(5)
print(my_list)