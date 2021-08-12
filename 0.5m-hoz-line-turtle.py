import turtle

WIDTH, HEIGHT = 1400, 560  # Width and height for turtles

screen = turtle.Screen()  # Setting up where turtle starts
screen.setup(WIDTH, HEIGHT)  # sets up window
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)  # turtle boundaries

flag = turtle.Turtle()  # Naming turtle

start = 200
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

meashoz= turtle.Turtle()
meashoz.penup() # So turtle doesnt draw lines
meashoz.goto(0, 80)  # Tells turtle where to start
meashoz.forward(160)  # Move forward to first dot spot
meashoz.pendown() #Puts pen down to draw line
meashoz.forward(40)  # Move forward to middle of dots
meashoz.write('0.5 Metres')  # Places Dot and color of dot
meashoz.forward(120) # Moves to next dot


turtle.done()
