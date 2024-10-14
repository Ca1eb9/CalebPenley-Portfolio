/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package;

/**
 *
 * @author calebpenley
 */
///
//PrimaryMortgage class is a subclass of LoanAccount and uses inheritance to organize different loan types
///
public class PrimaryMortgage extends LoanAccount {
    //init
    private double PMIMonthlyAmount;
    private Address Address;
    
    //constructor
    public PrimaryMortgage(double new_principal, double annual_int_rate, int months, double pmi_monthly_amount, Address address) {
        super(new_principal, annual_int_rate, months);
        PMIMonthlyAmount = pmi_monthly_amount;
        Address = address;
    }
    
    //string method to display info
    public String toString() {
        return "Primary Mortgage Loan"+super.toString()+"\nPMI Monthly Amount: $"+PMIMonthlyAmount+Address.toString();
    }
    
}
