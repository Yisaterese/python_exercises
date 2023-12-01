number = int(input("Enter number: "))
total = 0
count = 0
if(number == -3):
  print("bye")
else:
	while number != -3:
		total += number
		count += 1
		number = int(input("Enter number: "))
average = total/count
print("Average is ",average)

for char in "joseph":
	print(char)
name = "joseph"
print(name)
print(len("joseph"))