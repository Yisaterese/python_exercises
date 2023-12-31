even = 0
total = 0
for number in range(1,101):
	if(number % 2 == 0):
		total += number
		even = number
		print(even)
		
print()
print(total)