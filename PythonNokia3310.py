print("\tWelcome to Nokia ")
print("Date")
print("Time")
number = int(input("press 1 to display menu: "))
if(number == 1):
	print("1.Phone book")
	print("2.Messages")	
	print("3.Chat")	
	print("4.Call Register")	
	print("5.Tones")	
	print("6.Settings")	
	print("7.Call Divert")	
	print("8.Games")	
	print("9.Calculator")	
	print("10.Reminder")	
	print("11.Clock")
	print("12.Profiles")
	print("13.Sim Services")
if(number != 1):
	print("Enter a valid option")
menu = int(input("Select option to diaplay: "))
match menu:
	case 1:
		print("\tPHONEBOOK\n1.Search\n2.Service Nos\n3.Add name\n4.Erase\n5.Edit\n6.Assign tone\n7.Send b'card\n8.Options\n9.Speed dials\n10.Voice tags\n")
		phone_book = int(input("Enter number 1 to select options in phonebook"))
		match phone_book:
			case 1:
				print("Search")
			case 2:
				print("Service")
			case 3:
				print("Add name")
			case 4:
				print("Erase")
			case 5:
				print("Edit")
			case 6:
				print("Assign tone")
			case 7:
				print("Send b'card")
			case 8:
				print("option")
				option = int(input("Select between 1 and 2 for options"))
				match option:
					case 1:
						print("Type of view")
					case 2:
						print("Memory status")
				



















