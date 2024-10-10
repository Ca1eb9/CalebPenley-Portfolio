/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package compsci_221_pa3_cp;
import java.util.ArrayList;

/**
 *
 * @author calebpenley
 */
// Customer class to keep track of loan accounts per customer
public class Customer {
    //Init
    private String firstName;
    private String lastName;
    private String SSN;
    private ArrayList<LoanAccount> loanAccounts = new ArrayList<>();
    
    //Constructer
    public Customer(String first, String last, String ssn){
        firstName = first;
        lastName = last;
        SSN = ssn;
    }
    //Get Methods
    public String getfirstName(){
        return firstName;
    }
    public String getlastName(){
        return lastName;
    }
    public String getSSN(){
        return SSN;
    }
    //ArrayList add method
    public void addLoanAccount(LoanAccount account){
        loanAccounts.add(account);
    }
    //Monthly report that prints all accounta associated with the customer
    public void printMonthlyReport(){
        System.out.println("Account Report for Customer: "+firstName+" "+lastName+" with "+SSN+"\n");
        for(LoanAccount loanAccount:loanAccounts){
            System.out.println(loanAccount.toString());
        }
    }
}
