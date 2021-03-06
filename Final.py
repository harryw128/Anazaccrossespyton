import turtle

with open('crosses.txt') as f:
    # opens crosses fill and read lines
    lines = f.readlines()
print(lines)  # prints out names from txt file

cross_names = [s.replace("\n", "") for s in lines]  # removes /n after all names

print(cross_names)  # prints out new list
WIDTH, HEIGHT = 1400, 560  # Width and height for turtles

screen = turtle.Screen()  # Setting up where turtle starts
screen.setup(WIDTH, HEIGHT)  # sets up window
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)  # turtle boundaries

flag = turtle.Turtle()  # Naming turtle

start = 200 # Start point
flag.penup()  # So turtle doesnt draw lines
flag.goto(0, 100)  # Tells turtle where to start
for i in range(2):  # Loops twice so does 2 lines of dots
    for j in range(5):  # Loops 5 times to do 5 dots
        flag.penup()
        flag.forward(160)  # Move forward for dots
        flag.dot(10, "red")  # Places Dot and color of dot
        flag.penup()  # Puts dot back up

    flag.goto(0, start)  # Tells turtle where to go for 2nd line
    start = start + 100  # Adds 100 so turtle goes higher

names = turtle.Turtle()  # Names turtle
start = 205  # Where turtle starts
number = 0
names.penup()  # so doesn't do line
names.goto(0, 105)  # Start point
names.color('blue')  # text color
for i in range(2):  # Repeats twice for both rows
    for j in range(5):  # Repeats 5 for 5 names per row
        names.forward(160)  # Spaces between names/dots
        names.write(cross_names[number])  # Sorts list so names are spread out
        number += 1

    names.goto(0, start)  # Moves to 2nd line
    start = start + 105  # Command for what start is

meash = turtle.Turtle()
meash.penup()  # So turtle doesnt draw lines
meash.goto(0, 80)  # Tells turtle where to start
meash.forward(160)  # Move forward to first dot spot
meash.pendown()  # Puts pen down to draw line
meash.forward(40)  # Move forward to middle of dots
meash.write('0.5 Metres')  # Places Dot and color of dot
meash.forward(80)  # Moves to next dot

measv = turtle.Turtle()
measv.penup()  # So turtle doesnt draw lines
measv.goto(150, 100)  # Tells turtle where to start
measv.left(90) # Turn so can go up
measv.pendown()  # So draws lines
measv.forward(40) # Forward to forward
measv.write("   0.5 Metres") # Writes 0.5 metres
measv.forward(50) # Move forward to next row

turtle.done()
