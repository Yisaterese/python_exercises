number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))
number3 = int(input("enter third number:"))
if(number1 < number2 and number3):
 print("number1 is the minimum",number1)
if(number2 < number1 and number3):
 print("number number2 is the minimum",number2)
if(number3 < number1 and number2):
 print("number3 is the minimum",number3)