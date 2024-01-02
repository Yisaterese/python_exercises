def sum_of_numbers(my_list):
	sum = 0
	for index in my_list:
		sum += index
	return sum

def while_sum_of_numbers(list):
	sum = 0
	counter = 0
	while counter < list[len(list)-1]:
		sum += list[counter]
		counter +=1
	return sum	