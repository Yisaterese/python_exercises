number1 = int(input("Enter number: "))
product = 1 
count = 0
for number in range(number1):
    product **= number
    count +=1
print(product)
    