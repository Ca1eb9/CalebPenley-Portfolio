//Caleb Penley
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package compsci_221_pa3_cp;
import java.util.ArrayList;
//Loan account class intended to use create a an object of general loan details, and be able to have several subclasses
/**
 *
 * @author calebpenley
 */
public class LoanAccount {
    //Class init
    private double annualInterestRate;
    private double principal;
    private int months;
    
    //constructor
    public LoanAccount(double new_principal, double annual_int_rate, int months) {
        this.principal = new_principal;
        this.annualInterestRate = annual_int_rate/100.0;
        this.months = months;
    
    }
    
    //method used to calc monthly payments
    public double calculateMonthlyPayment(){
        double monthlyInterest = annualInterestRate/12;
        double monthlyPayment = principal * ( monthlyInterest / (1 - Math.pow(1 + monthlyInterest, -months)));
        return Math.round(monthlyPayment*100.00)/100.0; //including rounding to make sure output is 2 decimals
    }
    //get methods of properties
    public int getMonths(){
        return months;
    }
    
    public double getPrinciple() {
        return principal;
    }
    public double getAnnualInterestRate() {
        return annualInterestRate;
    }
    
    //method for returning class info
    public String toString() {
        return " with:\nPrincipal: $"+getPrinciple()+"\nAnnual Interest Rate: "+getAnnualInterestRate()*100.00+"%\nTerm of Loan in Months: "+getMonths()+"\nMonthly Payment: $"+calculateMonthlyPayment();
    }
    
    
    
    
    
    
    
    
    
    //testing code
    /**
     *
     * @param args
     */
    public static void main(String[] args) {
                // Create different loan objects, at least one of each type.
        CarLoan carLoan1 = new CarLoan(25000.00, 4.9, 72, "IRQ3458977");
        CarLoan carLoan2 = new CarLoan(12000.00, 5, 60, "NXK6767876");
        
        Address propertyAddress1 = new Address("321 Main Street", "State College", "PA", "16801");
        PrimaryMortgage propertyLoan1 = new PrimaryMortgage(250000.00, 3.75, 360, 35.12, propertyAddress1);
        Address propertyAddress2 = new Address("783 Maple Lane", "State College", "PA", "16801");
        PrimaryMortgage propertyLoan2 = new PrimaryMortgage(375000.00, 2.5, 360, 53.12, propertyAddress2);
        
        UnsecuredLoan unsecuredLoan = new UnsecuredLoan(5000.00, 10.75, 48);
        
        // create customers
        Customer customerA = new Customer("Tony", "Stark", "111-22-3333");
        Customer customerB = new Customer("Gal", "Gadot", "444-55-6666");
        
        // add loans for the customers.
        customerA.addLoanAccount(carLoan1);
        customerA.addLoanAccount(propertyLoan1);
        customerA.addLoanAccount(unsecuredLoan);
        
        customerB.addLoanAccount(carLoan2);
        customerB.addLoanAccount(propertyLoan2);
        
        // add the customers to an arraylist of customers.
        ArrayList<Customer> customers = new ArrayList<>();
        customers.add(customerA);
        customers.add(customerB);
        
        //Print out the loan information for each customer polymorhically.
        System.out.println("Monthly Report of Customers by Loan Account");
        for (Customer customer:customers)
        {
            customer.printMonthlyReport();
        }
    }
    
    
}
