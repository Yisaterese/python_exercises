def even_position(list):
	result = 0
	for index in list:
		if index % 2 == 0:
			result.append(index)
	return result	

def odd_position(list):
	result = 0
	for index in list:
		if index % 2 != 0:
			result.append(index)
	return result	
		