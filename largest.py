def largest1(m,n,k):
	if m > n and m > k:
		return m
	if n > m and n > k:
		return n
	if k > n and k > m:
		return k
print(largest1(60,56,200))

def largest2(m,n,k):
	result = 0
	if m > n and m > k:
		result = m
	if n > m and n > k:
		result = n
	if k > n and k > m:
		result = k
		return result
print(largest2(60,56,200))


def largest3(m,k,n,):
	largest = m
	if k > m: 
		largest = k
	if n > k :
		largest = n
	return largest
print(largest3(96,89,123))

def multiplication(m,k):
	return m * k
print(multiplication(2,4))

