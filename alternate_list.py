def alternate_list(list,my_list):
	result = []
	for i in zip(list,my_list):
		result.extend(i)
	return result	