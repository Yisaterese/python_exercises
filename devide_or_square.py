import math

def devide_or_square(x):
	result = math.sqrt(x)
	if x % 5 == 0:
		return result
	if x % 5 != 0:
		result1 = x % 5
		return result1