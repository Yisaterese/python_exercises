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
		phone_book = int(input("Enter number 1 to select options in phonebook: "))
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
				option = int(input("Select between 1 and 2 for options: "))
				match option:
					case 1:
						print("Type of view")
					case 2:
						print("Memory status")
			case 9:
				print("Speed dials")
			case 10:
				print("Voice tags")
	case 2:
		print("\tMESSAGES\n1.Write message\n2.Inbox\n3.Outbox\n4.Picture messages\n5.Templates\n6.Smileys\n7.Message settings\n8.Info services\n9.Voice mailbox number\n10.Service command editor\n")
		messages = int(input("select option between 1 and 10 for messages: "))
		match messages:
			case 1:
				print("Write Messages")
			case 2:
				print("Inbox")
			case 3:
				print("Outbox")
			case 4:
				print("Picture messages")
			case 5:
				pint("Templates")
			case 6:
				print("Smilleys")
			case 7:
				print("Message settings")
				message_settings = int(input("select between 1 and 2 for options in message settings: "))
				match message_settings:
					case 1:
						print("\tMessage settings\n1.Set\n2.Common\n")
						set = int(input("Press 1 or 2 select option: "))
						match set:
							case 1:
								print("\tSET\n1.Message centre number\n2.Messages sent as\n3.Message validity\n")
							case 2:
								print("\tCommon\n1.Delivery options\n2.Reply via same centre\n3.Character support\n")
			case 8:
				print("Info services")
			case 9:
				print("Voice mailbox number")
			case 10:
				print("Service command editor")
	case 3:
		print("Chat")
	case 4:
		print("Call register")
		call_register = int(input("press 1 to display options in call register: "))
		print("\tCall register\n1.Missed calls\n2.Received calls\n3.Dialed numbers\n4.Erase recent call lists\n5.Show call duration\n6.show call costs\n7.Call costs\n8.prepaid credit\n")

		register = int(input("press 1 to select options in call register:"))
		match register:
			case 1:
				print("Missed calls")
			case 2:
				print("Received calls")
			case 3:
				print("Dialled numbers")
			case 4:
				print("Erase recent calls lists")
			case 5:
				print("Show call duration")
				
				print("\tCALL DURATION\n1.last call duration\n2.All calls' duration\n3.Received calls' duration\n4.Dialled calls duration\n5.Clear times\n")
				call_duration = int(input("Enter number between 1 and 5 to select option in call duration: "))
				match call_duration:
					case 1:
						print("last call duration")
					case 2:
						print("All calls duration")
					case 3:
						print("Received calls' duration")
					case 4:
						print("Dialled calls' duration")
					case 5:
						print("Clear times")
			case 6:
				print("Show call costs")
				call_cost = int(input("press 1 to display options in call cost: "))
				print("\tShow call costs\n1.Last call cost\n2.All calls' cost\nClear counters\n")
				
				match call_cost:
					case 1:
						print("last call cost")
					case 2:
						print("All calls cost")
					case 3:
						print("Clear counters")
			case 7:
				print("Call cost settings")
				callcost_settings = int(input("Enter number to display call cost settings"))
				print("1.Call cost limit\n2.Show costs in")
				match callcost_settings:
					case 1:
						print("call cost linmit")
					case 2:
						print("Show costs in")
			case 8:
				print("Prepaid credit")
				
	case 5:
		print("Tones")
		tones = int(input("select between 1 and 9 for options in tones"))
		print("\tTONES\n1.Ringing tone\n2.Ringing volume\n3.Incoming call alert\n4.Composer\n5.Message alert tone\n6.Keypad tones\n7.	Warning and game tones\n8.Vibrating alarm\n9.Screen saver")
		match tones:
			case 1:
				print("Ringing tone")
			case 2:
				print("Ringing volume")
			case 3:
				print("Incoming call alert")
			case 4:
				print("Composer")
			case 5:
				print("Message alert tones")			
			case 6:
				print("Kepad tones")				
			case 7:
				print("Warning and game tones")
			case 8:
				print("Vibrating alert")		
			case 9:
				print("Screen saver")
	case 6:
		print("Settings")
		Settings = int(input("select between 1 and  to display options in settings"))
		print("\tSETTINGS\nCll settings\n2.Phone settings\n3.Security settings\n4.Restore factory settings: ")
		match settings:
			case 1:
				print("Call settings")
				call_settings = int("select between 1 and 6 to display options in call settings: ")
				print("\tCALL SETTINGS\n1.Automatic redial\n2.Speed dialing\n3.Call waiting options\n4.Own number sending\n5.Phpne line in use\n6.Automatic answer\n")
				match call_settings:
					case 1:
						print("Automatic redial")
				
					case 2:
						print("Speed redial")
					case 3:
						print("Call waiting options")
					case 4:
						print("Own number sending")
					case 5:
						print("phone line in use")
					case 6:
						print("automatic answer")
			case 2:
				print("Phone settings")
				Phone_settings = int(input("select between 1 and 6 to for options in phone settings: "))
				print("\tPHONE SETTINGS\n1.Lnguage\n2.Cell ifo info display\n3.Welcome note\n4.Network selection\n5.lights\n6.Confirm SIM service action")			
				match Phone_settings:
					case 1:
						print("Lnaguage")
					case 2:
						print("Cell info display")
					case 3:	
						print("Welcome note")
					case 4:
						print("Network selection")
					case 5:
						print("Lights")
					case 6:
						print("Confirm 	SIM service action")
			case 3:
				print("Security settings")
				Security_settings = int(input("select between 1 and 6 for options in security settings: "))
				print("\tSECURITY SETTINGS\n1.PIN code request\n2.Call barring services\n3.Fixed dialing\n4.Closed user services\n5.Phone security\n6.Change access codes")
				match Security_settings:
					case 1:
						print("PIN code request")
					case 2:
						print("Call barring services")
					case 3:
						print("Fixed dialing")
					case 4:
						print("Closed user group")
					case 5:
						print("Phone security")
					case 6:
						print("Change access codes")
	case 7:	
		print("Call divert")
	case 8:
		print("Games")
	case 9:
		print("Calculator")
	case 10:
		print("Reminders")
	case 11:
		print("Clock")
		clock = int(input("select between 1 and 6 for options in clock: "))
		print("\tCLOCK\n1.Alarm clock\n2.Clock settings\n3.Date settings\n4.Stopwatch\n5.Countdown timer\n6.Auto update of date and time")	

		match clock:
			case 1:
				print("Alarm")
			case 2:
				print("Clock settings")

			case 3:
	
				print("Date settings")
			case 4:
				print("Stopwatch")
			case 5:
				print("Countdown timer")

			case 7:

				print("Auto update of date and time")
	case 12:
		print("Profiles")
	case 13:
		print("SIM services")



				
















