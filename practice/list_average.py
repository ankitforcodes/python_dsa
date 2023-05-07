# Ask user how many days of temperature that they want to enter
# Get all the days of temperature
# Return 2 tihngs
# a. Avg of those temperatures
# b. No. of days for which the temperature was more than the avg

n = int(input('How many days do you want to ender?'))
temperatures = []
for i in range(n):
	temp = int(input("Enter temperature"))
	temperatures.append(temp)


avg_temp = sum(temperatures)/ len(temperatures)

c = 0

for items in temperatures:
	if items > avg_temp:
		c = c + 1

print("Avg temp: ", avg_temp)
print("day above avg: ", c)
