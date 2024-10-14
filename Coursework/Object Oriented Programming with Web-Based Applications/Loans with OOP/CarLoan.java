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
//CarLoan class is a subclass of LoanAccount and uses inheritance to organize loans
///
public class CarLoan extends LoanAccount {
    //init
    private String vehicleVIN;
    //constructor
    public CarLoan(double new_principal, double annual_int_rate, int months, String vehicle_vin){
        super(new_principal, annual_int_rate, months);
        vehicleVIN = vehicle_vin;
    }
    //string method for displaying info
    public String toString() {
        return "Car Loan"+super.toString()+"\nVehicle VIN: "+vehicleVIN+"\n\n";
    
    }
    
}
