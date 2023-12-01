number1 = int(input("Enter number (enter 0 to end): ")) 

sum = 0
total = 0
count = 0
while number1 != 0:
    total += number1
    count += 1 
    number1 = int(input("Enter number (enter 0 to end): ")) 
   
    average = total/count
    sum = total
print("average: ",average)
print("sum: ",sum)