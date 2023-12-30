import random
guess = 1

for guess in range(5):
	guess = int(input("Enter guess: "))
	result =random.randrange(1,10)
	print("random number is", result)
	if(guess == result): 
		print("YOU WIN")
		break
	if(guess != result): 
		print("Try again")