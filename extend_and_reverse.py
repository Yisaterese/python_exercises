def extend_and_reverse(list,my_list):

	list.extend(my_list)
	list.reverse()
	return list

def extend_and_reverse2(list,my_list):
	
	return (list + my_list)[:: -1]

def extend_and_reverse3(list,my_list):
	x = list + my_list
	x.reverse()
	return x