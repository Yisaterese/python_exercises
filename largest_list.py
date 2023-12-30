for i in range(n,k,m):
		largest = n
		if k > largest:
			largest = k
		if m > k:
			largest = m
print(largest)