evenNumbers = 0
oddNumbers = 0
total = 0
count = 0
number = 100
while count <= 100:
	count += 1
	if(count % 2 == 0):
		print(evenNumbers) 

	if(count % 2 != 0):
		print(oddNumbers)
	
	count += 1
	total += count
print(total,evenNumbers,oddNumbers)