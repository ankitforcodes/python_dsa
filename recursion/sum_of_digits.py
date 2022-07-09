'''
12345 = 1 + 2 + 3 + 4 + 5 = 15
123 = 1 + 2 + 3 = 6
1 = 1
12 = 1 + 2 = 3
'''

def sumOfDigits(n):
	if n%10 == n:
		return n
	else:
		sum = n%10 + sumOfDigits(n//10)
		return sum

print(sumOfDigits(31))

