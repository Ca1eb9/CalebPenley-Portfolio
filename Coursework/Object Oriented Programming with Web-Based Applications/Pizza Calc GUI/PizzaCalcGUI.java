
//Caleb Penley
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package cmpsc_221_pa4_cp;
//Import required packages
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import javax.swing.border.*;

/**
 *
 * @author calebpenley
 */
//PizzaCalcGUI class to allow ease of access to a pizza slice calculator that determines the amount of servings from the size of pizza
public class PizzaCalcGUI extends JFrame{
    //declare private vars
    private final JLabel slicesLabel;
    private final JLabel pizzaTitle;
    private final JTextField slicesField;
    private final JLabel servingsLabel;
    private final JButton calcButton;
    private final JPanel line1;
    private final JPanel line2;
    private final JPanel line4;
    private double servings;
    
    //Constructor
    public PizzaCalcGUI(){
        //initilizing the GUI's objects using swing and awt
        super("Pizza Servings Calculator"); //frame title
        setLayout(new GridLayout(4,1));
        pizzaTitle = new JLabel("Pizza Servings Calculator");
        pizzaTitle.setFont(new Font("Times New Roman", Font.PLAIN, 26)); //increase font and times new roman like example
        pizzaTitle.setForeground(Color.RED); // red font like example
        pizzaTitle.setHorizontalTextPosition(SwingConstants.CENTER);
        pizzaTitle.setVerticalTextPosition(SwingConstants.BOTTOM);
        slicesLabel = new JLabel();
        slicesLabel.setText("Enter the size of the pizza in inches:");
        slicesField = new JTextField(4);
        calcButton = new JButton("Calculate Servings");
        servingsLabel = new JLabel();
        servingsLabel.setHorizontalTextPosition(SwingConstants.CENTER);
        servingsLabel.setVerticalTextPosition(SwingConstants.BOTTOM);
        CalcButtonHandler handler = new CalcButtonHandler(); // Button Handler
        calcButton.addActionListener(handler);
        //////
        //Create panel objects to help correctly display each component in the gui
        line1 = new JPanel(new BorderLayout());
        line2 = new JPanel();
        line4 = new JPanel();
        line1.setBorder(new EmptyBorder(20, 35, 20, 0)); // creates margins to suspend the object in the middle of the panel
        line4.setBorder(new EmptyBorder(20, 0, 20, 0));
        ///////
        //add each component (JLabel, JTextField, etc) to their respective panel
        line1.add(pizzaTitle);
        line2.add(slicesLabel);
        line2.add(slicesField);
        line4.add(servingsLabel);
        //add each panel to the frame
        add(line1);
        add(line2);
        add(calcButton);
        add(line4);
}       //
    //Button handler class to handle listening events of button
    private class CalcButtonHandler implements ActionListener 
    {
        //method to perform the calculation upon button
        @Override
        public void actionPerformed(ActionEvent event)
        {
        //try and catch usage to prevent the program from crashing if anything other than digits are in the text field when button pressed
        try {
            servings = Math.pow(Double.parseDouble(slicesField.getText())/8,2);
            servingsLabel.setText("A "+slicesField.getText()+" inch pizza will serve "+servings+" people."); // update text field with new servings calculation
        } catch (Exception e) {
            servingsLabel.setText("Please input a number only"); // reiterate the need for numbers in the text box
        }
        
        }

}
        
        
    
}
