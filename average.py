number = int(input("please enter number or -1 to stop:  "))

total =  0
count = 0
number = 0
while number != -1:
	total += number 
	count += 1
	number = int(input("please enter number or -1 to stop:  "))
average = total/count
sum = number + count
print(average,sum)