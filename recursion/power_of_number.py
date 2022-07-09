'''
x ^ y = x * x * x * x (y times)
2 ^ 3 = 2 * 2 * 2

Logic:
Recursion: 2 ^ n = 2 * 2^(n-1)
Break: 2 ^ 0 = 1 and 2 ^ 1 = 2
'''


def powerOfNum(x,y):
	if y == 0:
		return 1
	elif y == 1:
		return x
	else:
		return x * powerOfNum(x, y-1)

print(powerOfNum(2,4))
