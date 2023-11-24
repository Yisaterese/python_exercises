public class AccountTest{
public static void main(String[] args){

Account account = new Account();

String nameOfAccount = account.setName("Joseph Yisa ");

String accountNumber = account.setAccountNumber("34566");

System.out.printf("The name of the account is %s%nThe account number is %s",nameOfAccount,accountNumber); 
}
}