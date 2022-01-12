# Project:      Final Project (BunnaPhearakBothSec02Ver03.py)
# Name:         Phearak Both Bunna
# Date:         10/03/20
# Description:  This program will allow the user to
#               throw 5 dice and get the intTotal value
#               of the 5 dice
#               This is my very first programming project for Intro to Python class

from graphics import *
import random

def RandomNum(win,k, intRand):

    # Call the Dice function
    Dice(win,k)

    # Call the dot function for 1st Dice
    if intRand == 1:
        Dot7(win,k)

    # Call 2 dot functions for 2nd Dice
    elif intRand == 2:
        Dot3(win,k)
        Dot4(win,k)

    # Call 3 dot functions for 3rd Dice
    elif intRand == 3:
        Dot7(win,k)
        Dot3(win,k)
        Dot4(win,k)

    # Call 4 dot functions for 4th Dice
    elif intRand == 4:
        Dot1(win,k)
        Dot3(win,k)
        Dot4(win,k)
        Dot6(win,k)

    # Call 5 dot functions for 5th Dice
    elif intRand == 5:
        Dot1(win,k)
        Dot3(win,k)
        Dot4(win,k)
        Dot6(win,k)
        Dot7(win,k)

    # Call 6 dot functions for 6th Dice
    elif intRand == 6:
        Dot1(win,k)
        Dot2(win,k)
        Dot3(win,k)
        Dot4(win,k)
        Dot5(win,k)
        Dot6(win,k)

def Dice(win,k):

    # Set the points of the dice with constant Y coordinates
    # and increasing X coordinates
    # k loops 6 times and 150 * k is distance between 2 dice
    dice = Rectangle(Point(40 + 150 * k, 50), Point(170 + 150 * k, 170))

    # Set the dice to white
    dice.setFill("white")

    # Draw the dice
    dice.draw(win)

def Dot1(win,k):

    # Draw the dot for the dice with constant Y coordinates
    # and increasing X coordinates
    # 150 * k is the distance between the dots of 2 dice
    dot1 = Circle(Point(60 + 150 * k, 70), 10).draw(win)

    # Set the dot color to black
    dot1.setFill("black")

def Dot2(win,k):

    # Draw the dot for the dice with constant Y coordinates
    # and increasing X coordinates
    dot2 = Circle(Point(60 + 150 * k, 110), 10).draw(win)
    dot2.setFill("black")

def Dot3(win,k):

    # Draw the dot for the dice with constant Y coordinates
    # and increasing X coordinates
    dot3 = Circle(Point(60 + 150 * k, 150), 10).draw(win)
    dot3.setFill("black")

def Dot4(win,k):

    # Draw the dot for the dice with constant Y coordinates
    # and increasing X coordinates
    dot4 = Circle(Point(150 + 150 * k, 70), 10).draw(win)
    dot4.setFill("black")

def Dot5(win,k):

    # Draw the dot for the dice with constant Y coordinates
    # and increasing X coordinates
    dot5 = Circle(Point(150 + 150 * k, 110), 10).draw(win)
    dot5.setFill("black")

def Dot6(win,k):

    # Draw the dot for the dice with constant Y coordinates
    # and increasing X coordinates
    dot6 = Circle(Point(150 + 150 * k, 150), 10).draw(win)
    dot6.setFill("black")

def Dot7(win,k):

    # Draw the dot for the dice with constant Y coordinates
    # and increasing X coordinates
    dot7 = Circle(Point(105 + 150 * k, 110), 10).draw(win)
    dot7.setFill("black")

def main():

    # Draw the graphic window with khaki background
    win = GraphWin("Dice", 800, 400)
    win.setBackground('khaki')

    # Draw the white exit button
    exitButton = Rectangle(Point(720, 360), Point(790, 390))
    exitButton.setFill("white")
    exitButton.draw(win)

    # Draw the exit label and increase the size
    exitLabel = Text(Point(755, 375), "EXIT")
    exitLabel.setSize(15)
    exitLabel.draw(win)

    # Lists of the dice labels
    lstDiceLabel = ["Dice1", "Dice2", "Dice3", "Dice4", "Dice 5"]

    # Initialize the value of i
    i  = 0

    # Running intTotal by adding 20 each time
    i += 20

    for j in range(5):

        # Set the top X and Y coordinates for the outline
        # j * 150 is the distance between 2 outlines
        # i is the blank space between the outlines
        ptXtop = 20 + (j * 150) + i
        ptYtop = 50

        # Set the bottom X and Y coordinates for the outline
        ptXbot = 170 + (j * 150)
        ptYbot = 170

        # Set the X and Y coordinates for the outline label
        ptLabelX = 105 + (j * 150)
        ptLabelY = 110

        # Draw the outline labels from the labels list
        diceLabel = Text(Point(ptLabelX, ptLabelY), lstDiceLabel[j])
        diceLabel.setTextColor("grey")
        diceLabel.setStyle("bold")
        diceLabel.draw(win)

        # Set the dice outline using the coordinates from above
        diceOutline = Rectangle(Point(ptXtop, ptYtop), Point(ptXbot, ptYbot))

        # Set the outline to light grey
        diceOutline.setOutline("light grey")

        # Increase the width and draw
        diceOutline.setWidth(10)
        diceOutline.draw(win)

    # Initialize the value
    intTotal = 0

    # Draw the dice total text
    intTotalLabel = Text(Point(250, 200), "Dice Total")
    intTotalLabel.setTextColor("red")
    intTotalLabel.draw(win)

    # Display the initial total value
    valueLabel = Text(Point(250, 220), intTotal)
    valueLabel.setTextColor("red")
    valueLabel.draw(win)

    restButton = Rectangle(Point(50, 360), Point(150, 390))
    restButton.setFill("white")
    restButton.draw(win)

    restLabel = Text(Point(100, 375), "RESTART")
    restLabel.setTextColor("black")
    restLabel.setStyle("bold")
    restLabel.draw(win)


    for k in range(6):

        # Get the mouse click from the user 6 times
        getPtxy = win.getMouse()

        # Get the X and Y coordinates of the click
        ptX = getPtxy.getX()
        ptY = getPtxy.getY()

        # When click on the 1st dice
        if 40 < ptX < 170 and 50 < ptY < 170:

            # Generate random number from 1 to 6
            intRand = random.randint(1, 6)

            # Call the function
            RandomNum(win,k, intRand)

            # Display the dice running total
            intTotal += intRand
            valueLabel.setText(intTotal)

        # When click on the 2nd dice
        elif 190 < ptX < 320 and 50 < ptY < 170:

            # Generate random number
            intRand = random.randint(1, 6)

            # Call the function
            RandomNum(win,k, intRand)

            # Display the dice running total
            intTotal += intRand
            valueLabel.setText(intTotal)

        # When click on the 3rd dice
        elif 340 < ptX < 470 and 50 < ptY < 170:

            # Generate random number
            intRand = random.randint(1, 6)

            # Call the function
            RandomNum(win,k, intRand)

            # Display the dice running total
            intTotal += intRand
            valueLabel.setText(intTotal)

        # When click on the 4th dice
        elif 490 < ptX < 620 and 50 < ptY < 170:

            # Generate random number
            intRand = random.randint(1, 6)

            # Call the function
            RandomNum(win,k, intRand)

            # Display the dice running total
            intTotal += intRand
            valueLabel.setText(intTotal)

        # When click on the 5th dice
        elif 650 < ptX < 770 and 50 < ptY < 170:

            # Generate random number
            intRand = random.randint(1, 6)

            # Call the function
            RandomNum(win,k, intRand)

            # Display the dice running total
            intTotal += intRand
            valueLabel.setText(intTotal)

            if intTotal > 9:

                # Display a congrats message for the user
                congratsMes = Text(Point(250, 250), "You are lucky!")
                congratsMes.setTextColor("red")
                congratsMes.draw(win)

        # When click on the exit button
        if 720 < ptX < 790 and 360 < ptY < 390:

            # Close the window
            win.close()

        if 50 < ptX < 150 and 360 < ptY < 390:

            main()
main()
