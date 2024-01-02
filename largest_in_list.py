def largest_in_list(my_list):

	##largest = my_list[-1]

	largest = my_list[len(my_list)-1]
	for index in my_list:
		if index > largest:
			largest = index
	return largest

def min_in_list(my_list):

	min = my_list[-1]

	##largest = my_list[len(my_list)-1]
	for index in my_list:
		if index < min:
			min = index
	return min