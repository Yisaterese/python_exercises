
def front_screen():
	print ("1.Date\n2.Time")
	print(front_screen())	
	
def menu():
	print( "\tMENU\n1.Phonebook\n2.Messages\n3.Chat\n4.Call register\n5.Tones\n6.Settings\n7.Call divert\n8.Games\n9.Calculate\n10.Reminders\n11.Clock\n12.Profiles\n13.SIM services")	
		
	menu = (input("Select between 1 and 13 for options in menu: "))
	match menu:
		case "1":
			print("\tPHONEBOOK")
			print(phonebook_menu())

def phonebook_menu():
	print("1.Search\n2.Service\n3.Add name\n4.Ease\n5.Edit\n6.Assign tone\n7.Send b;card\n8.OPtion\n9.Speed dials\n10.Voice tags")
	if phonebook_menu == 2:
		return menu() 
		
			
			
print( menu())

def phonebook():
	print("1.Search\n2.Service\n3.add name\n4.Erase\n5.Edit\n6.Assign tone\n7.Send b;card\n8.Options\n9.Speed dials\n10.Voice tags")	
	print(phonebook())