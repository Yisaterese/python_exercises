import java.util.Scanner;

public class Nokia{
public static void main(String[] args){

Scanner scaner = new Scanner(System.in);

	System.out.println("1.Phone book");	
	System.out.priSntln("2.Messages");	
	System.out.println("3.Chat");	
	System.out.println("4.Call Register");	
	System.out.println("5.Tones");	
	System.out.println("6.Settings");	
	System.out.println("7.Call Divert");	
	System.out.println("8.Games");	
	System.out.println("9.Calculator");	
	System.out.println("10.Reminder");	
	System.out.println("11.Clock");	
	System.out.println("12.Profiles");	
	System.out.println("13.Sim Services");	
	
System.out.println("Enter choice for menu");
int menu = scanner.nextInt();

while (menu != -1){
	switch(menu){
		case 1:
			System.out.println("Phone book");
			break;
			switch(phonebook){
				case 1:
					System.out.print("Search");
					break;
					}
				case 2:
					System.out.println("Service Nos");
					break;
				case 3:
					System.out.println("Add name");
					break;
				case 4:
					System.out.print("Erase");
					break;
				case 5:
					System.out.println("Edit");
					break;
				case 6:
					System.out.println("Assign tone");
					break;
				case 7:
					System.out.println("Send b'Card");
					break;
				case 8: 
					System.out.println("Options");
					break;
					switch(Option){
						case 1: 
							System.out.println("Type of view");
							break;
						case 2:
							System.out.println("Memoery status");
							break;
						default:
							System.out.println("please enter a valid option");
						}
					break;
				case 9: 
					System.out.println("Speed dials");
					break;
				case 10:
					System.out.println("Voice stage");
					break;
			default:
				System.out.println("Please enter a valid 0ption");
			}
			break;
		case 2:

			switch(messages){
				case 1:
					System.out.println("Write messages");
					break;
				case 2:
					System.out.println("Inbox");
					break;	
				case 3:
					System.out.println("Outbox");
					break;
				case 4:
					System.out.println("Picture messages");
					break;
				case 5:
					System.out.println("Templates");
					break;
				case 6:
					System.out.println("Smileys");
					break;
				case 7:
					System.out.println("Message settings");
					break;
					switch(Message settings){
						case 1:
							System.out.println("set");
							break;
							switch(set){
								case 1:
									System.out.println("Message centre number");
									break;
								case 2:
									System.out.println("Message sent as");
									break;
								case 3:
									System.out.println("Message validity");
									break;
								default:
									System.out.println("Enter a valid option");
								}
								break;
						case 2:
							System.out.println("Common");
							break;
							switch(common){
								case 1:
									System.out.println("Delivery reports"):
									break;
								case 2:
									System.out.println("Reply via same centre");
									break;
								case 3:
									System.out.println("Character support");
									break;
								default:
									System.out.println("Enter a valid option");
								}
								break;
				case 8:
					System.out.println("Info services");
					break;
				case 9:
					System.out.println("Voice mailbox number");
					break;
				case 10:
					System.out.println("Service command editor");
					break;
				default:
					System.out.println("Enter a valid option");
				}
				break;
		case 3:
			switch(chat){
				System.out.println("chat");
				break;
				}
		case 4:
			switch(call register){
				case 1:
					System.out.println("Missed calls");
					break;
				case 2:
					System.out.println("Received calls");
					break;
				case 3:
					System.out.println("Dialled numbers");
					break;
				case 4:	
					System.out.println("Erase recent call list");
					break;
				case 5:
					Syste.out.println("Show call duration");
					break;
					switch(show call duration){
						case 1:
							System.out.println("Last call duration");
							break;
						case 2:
							System.out.println(""All calls duration);
							break;
						case 3:
							System.out.println("Received calls duration");
							break;
						case 4:
							System.out.println("Dialed calls duration");
							break;
						case 5:
							System.out.println("Clear timers");
							break;
						default:
							System.out.print("Enter a valid option");
				
					}
					break;
				case 6:
					System.out.println("Show call cost");
					break;
					switch(show call cost){
						case 1:
							System.out.println("Last call cost");
							break;
						case 2:
							System.outprint("All calls cost");
							break;
						case 3:
							System.out.println("Clear counters");
							break;
						default:
							System.out.print("Enter a valid optiion");
						}
						break;
				case 7:
					System.out.println("Call cost settings");
					break;
					switch(Call cost settings){
						case 1:
							System.out.println("Call cost limit");
							break;
						case 2:
							System.out.println("Show cost in");
							break;
						default:
							System.out.println("Enter a valid option");
						}
						break;
				case 8:
					System.out.println("Prepaid credit");
					break;		
					
			


		}
	}
}
}
