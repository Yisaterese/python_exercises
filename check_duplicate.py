def check_duplicate(my_stringlist):
	
	for i in my_stringlist:
		
		if i in my_stringlist:
			return my_stringlist.append(i)
		else:
			
			return print("No duplicate") 