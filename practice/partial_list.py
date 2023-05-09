# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
# myList = [1, 2, 3, 4]
# middle(myList)  # [2,3]

def middle(lst):
    # Return a new list containing all elements from the original list, excluding the first and last elements
    return lst[1:-1]