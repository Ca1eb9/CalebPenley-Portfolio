// Caleb Penley
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package java2ddrawingapplication;


import java.awt.BasicStroke;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.GradientPaint;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.GridLayout;
import java.awt.Paint;
import java.awt.Point;
import java.awt.Stroke;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.MouseMotionListener;
import java.util.ArrayList;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JColorChooser;
import javax.swing.JComboBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.JSpinner;
import javax.swing.*;

/**
 *
 * @author calebpenley
 */
//CP
//Drawing2D shapes application frame
public class DrawingApplicationFrame extends JFrame
{

    // Create the panels for the top of the application. One panel for each
    // line and one to contain both of those panels.
    private JPanel firstline;
    private JPanel secondline;
    private JPanel topPanel;
    private JPanel drawPanel;
    
    // create the widgets for the firstLine Panel.
    private JLabel shapeLabel;
    private JComboBox<String> shapeComboBox;
    private JButton color1Button;
    private JButton color2Button;
    private JButton undoButton;
    private JButton clearButton;
    //create the widgets for the secondLine Panel.
    
    private JLabel optionsLabel;
    private JCheckBox fillCheckBox;
    private JCheckBox gradientCheckBox;
    private JCheckBox dashedCheckBox;
    private JSpinner lineWidthSpinner;
    private JSpinner dashLengthSpinner;
    // Variables for drawPanel.
    
    private MyShapes currentShape;
    private Color color1 = Color.BLACK;
    private Color color2 = Color.BLACK;
    private ArrayList<MyShapes> shapes = new ArrayList<>();

    // add status label
    private JLabel statusLabel;
    // Constructor for DrawingApplicationFrame
    public DrawingApplicationFrame()
    {
        super("Java 2D Drawings");
        
        //init
        shapeLabel = new JLabel("Shape:");
        firstline = new JPanel(new FlowLayout());
        secondline = new JPanel(new FlowLayout());
        topPanel = new JPanel(new GridLayout(2, 1));
        topPanel.setBackground(Color.CYAN);
        topPanel.setOpaque(true);
        
        drawPanel = new DrawPanel();
        statusLabel = new JLabel();
        
        String[] shapesArray = {"Line", "Oval", "Rectangle"};
        optionsLabel = new JLabel("Options: ");
        shapeComboBox = new JComboBox<>(shapesArray);
        color1Button = new JButton("1st Color...");
        color2Button = new JButton("2nd Color...");
        undoButton = new JButton("Undo");
        clearButton = new JButton("Clear");
        fillCheckBox = new JCheckBox("Filled");
        gradientCheckBox = new JCheckBox("Use Gradient");
        dashedCheckBox = new JCheckBox("Dashed");
        lineWidthSpinner = new JSpinner(new SpinnerNumberModel(4,1,70,1));
        dashLengthSpinner = new JSpinner(new SpinnerNumberModel(15,1,70,1));
        
        // add widgets to panels
        
        // firstLine widgets
        firstline.add(shapeLabel);
        firstline.add(shapeComboBox);
        firstline.add(color1Button);
        firstline.add(color2Button);
        firstline.add(undoButton);
        firstline.add(clearButton);
        // secondLine widgets
        secondline.add(optionsLabel);
        secondline.add(fillCheckBox);
        secondline.add(gradientCheckBox);
        secondline.add(dashedCheckBox);
        secondline.add(new JLabel("Line Width:")); //for simplicity sake
        secondline.add(lineWidthSpinner);
        secondline.add(new JLabel("Dash Length:"));
        secondline.add(dashLengthSpinner);
        // add top panel of two panels
        topPanel.add(firstline);
        topPanel.add(secondline);
        // add topPanel to North, drawPanel to Center, and statusLabel to South
        
        add(topPanel, BorderLayout.NORTH);
        add(drawPanel, BorderLayout.CENTER);
        add(statusLabel, BorderLayout.SOUTH);
        
        //add listeners and event handlers
        
        //Lambda expressions for simplicity
        //Use JColorChooser for color selection
        color1Button.addActionListener(e -> color1 = JColorChooser.showDialog(this, "Choose 1st Color", color1));
        color2Button.addActionListener(e -> color2 = JColorChooser.showDialog(this, "Choose 2nd Color", color2));
        
        //undo button to remove last shape if arraylist is not empty
        undoButton.addActionListener(e -> {
           
            if (!shapes.isEmpty()) {
                shapes.remove(shapes.size() - 1);
                repaint();
            }
        });
        //Clear all shapes
        clearButton.addActionListener(e -> {shapes.clear();repaint();});
    }

    // Create event handlers, if needed

    // Create a private inner class for the DrawPanel.
    private class DrawPanel extends JPanel
    {

        public DrawPanel()
        {
            //init handler for mouse movements
            
            MouseHandler handler = new MouseHandler();
            addMouseListener(handler);
            addMouseMotionListener(handler);
        }

        public void paintComponent(Graphics g)
        {
            super.paintComponent(g);
            Graphics2D g2d = (Graphics2D) g;

            //loop through and draw each shape in the shapes arraylist
            //draw all shapes from the list
            for (MyShapes shape : shapes) {
                shape.draw(g2d);
            }

            //if a shape is being created, draw it
            if (currentShape != null) {
                currentShape.draw(g2d);
            }
        }

        //Mouse handler class
        private class MouseHandler extends MouseAdapter implements MouseMotionListener
        {

            public void mousePressed(MouseEvent event)
            {
                Point startPoint = event.getPoint();

                //Get the shape type from combo box
                String shapeType = (String) shapeComboBox.getSelectedItem();

                //Set stroke and paint properties from current spinner values
                float lineWidth = ((Number) lineWidthSpinner.getValue()).floatValue();
                float dashLength = ((Number) dashLengthSpinner.getValue()).floatValue();
               
                //Create current stroke
                Stroke stroke;
                
                //Create dashed stroke if need be
                if (dashedCheckBox.isSelected()) {
                    stroke = new BasicStroke(lineWidth, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND, 10, new float[]{dashLength}, 0);
                } else {
                    stroke = new BasicStroke(lineWidth, BasicStroke.CAP_ROUND, BasicStroke.JOIN_ROUND);
                }
                
                //Create gradient painting type if need be
                Paint paint;
                if (gradientCheckBox.isSelected()) {
                    paint = new GradientPaint(0, 0, color1, 50, 50, color2, true);
                } else {
                    paint = color1;
                }

                boolean isFilled = fillCheckBox.isSelected();
                
                //Create the shape based on current user selection from combo box
                switch (shapeType) {
                    case "Line":
                        currentShape = new MyLine(startPoint, startPoint, paint, stroke);
                        break;
                    case "Oval":
                        currentShape = new MyOval(startPoint, startPoint, paint, stroke, isFilled);
                        break;
                    case "Rectangle":
                        currentShape = new MyRectangle(startPoint, startPoint, paint, stroke, isFilled);
                        break;
                }
            }
            @Override
            public void mouseReleased(MouseEvent event)
            {
                //stop painting
                shapes.add(currentShape);
                currentShape = null;
                repaint();
            }

            @Override
            public void mouseDragged(MouseEvent event)
            {
                //creating the shape as mouse moves
                Point currentPoint = event.getPoint();
                currentShape.setEndPoint(currentPoint);
                repaint();
            }

            @Override
            public void mouseMoved(MouseEvent event)
            {
                //Displaying coords
                statusLabel.setText(String.format("(%d, %d)", event.getX(), event.getY()));
            
            }
        }

    }
}
