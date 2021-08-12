import turtle

# Width and height for turtles
WIDTH, HEIGHT = 1400, 560

# Setting up where turtle starts
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # sets up window
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)  # turtle boundires

flag = turtle.Turtle()  # Naming turtle

start = 200
flag.penup()  # So turtle doesnt draw lines
flag.goto(0, 100)  # Tells turtle where to start
for i in range(2):  # Loops twice so does 2 lines of dots
    for j in range(5):  # Loops 5 times to do 5 dots
        flag.penup()
        flag.forward(160)  # Move forward for dots
        flag.dot()  # Places Dot
        flag.penup()  # Puts dot back up

    flag.goto(0, start)  # Tells turtle where to go for 2nd line
    start = start + 100  # Adds 100 so turtle goes higher

turtle.done()  # Tells turtle its finshed
