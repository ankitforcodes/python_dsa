

t1 = ('a', 'b', 'c', 'd', 'e','d')

# O(n)
# Finding element in a tuple
x = 'a' in t1
print(x)


# Find index at which an element is stored in tuple
x = t1.index('c')
print(x)


# Find frequency of an element
x = t1.count('d')
print(x)