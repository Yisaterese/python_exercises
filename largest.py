def largest1(m,n,k):
	if m > n and m > k:
		return m
	if n > m and n > k:
		return n
	if k > n and k > m:
		return k
#print(largest1(60,56,200))




def largest2(m,n,k):
	result = 0
	if m > n and m > k:
		result = m
	elif n > m and n > k:
		result = n
	elif k > n and k > m:
		result = k
	return result
#print(largest2(60,56,200))


def largest3(m,k,n,):
	largest = m
	if n > k :
		largest = n
	elif k > n:
		largest = k
	return largest
#print(largest2(67,98,23))

def product(a, b):
	return a*b
#print(product(3, 3))