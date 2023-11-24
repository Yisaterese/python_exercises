import java.util.Scanner;
 
public class  Age{

public static void main(String[] args){
Scanner input = new Scanner(System.in);
System.out.println("Enter age in years");
int age = input.nextInt();

int ageInDays = age * 365;

System.out.printf("age in days is: %d", ageInDays);


}



}