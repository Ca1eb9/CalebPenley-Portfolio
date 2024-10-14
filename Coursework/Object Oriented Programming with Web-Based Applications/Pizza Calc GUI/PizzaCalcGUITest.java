/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package;
// import required package
import javax.swing.JFrame;

/**
 *
 * @author calebpenley
 */
// testing class to test PizzaCalcGUI
public class PizzaCalcGUITest {
    //testing code
    /**
     *
     * @param args
     */
    public static void main(String[] args) {
        //Default swing gui init
        PizzaCalcGUI pizzaGUI = new PizzaCalcGUI();
        pizzaGUI.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        pizzaGUI.setSize(350,300);
        pizzaGUI.setVisible(true);
    }
}
