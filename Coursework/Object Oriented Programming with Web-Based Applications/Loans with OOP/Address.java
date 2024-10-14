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
//Address class is intended to format and "objectify" an inputted address to be ready to be displayed
///
public class Address {
    //init
    private String street;
    private String city;
    private String state;
    private String zipCode;
    
    //constructor
    public Address(String st,String _city,String _state,String zip) {
        street = st;
        city = _city;
        state = _state;
        zipCode = zip;
    }
    
    //string method to display info
    public String toString() {
        return "\nProperty Address:\n\t"+street+"\n\t"+city+", "+state+" "+zipCode+"\n\n";
    }
}
