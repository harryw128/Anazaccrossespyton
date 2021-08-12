import turtle

with open('crosses.txt') as f:  # opens crosses fill and read lines
    lines = f.readlines()  # Reads lines
print(lines)  # prints out names from txt file

crossnames = [s.replace("\n", "") for s in lines]  # removes /n after all names

print(crossnames)  # prints out new list

WIDTH, HEIGHT = 1400, 560  # Width and height for turtles

screen = turtle.Screen()  # Setting up where turtle starts
screen.setup(WIDTH, HEIGHT)  # sets up window
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)  # turtle boundires

names = turtle.Turtle()  # Name turtle
start = 200  # Height Where turtle starts
number = 0
names.penup()  # so doesn't do line
names.goto(0, 50)  # Start point
for i in range(2):  # Repeates twice for both rows
    for j in range(5):  # Repeats 5 for 5 names per row
        names.forward(160)  # Spaces between names/dots
        names.write(crossnames[number])  # Sorts list so names are spread out
        number += 1

    names.goto(0, start)  # Moves to 2nd line
    start = start + 50

turtle.done()  # Tells turtle its finshed
