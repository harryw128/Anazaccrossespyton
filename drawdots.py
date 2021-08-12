import turtle
WIDTH, HEIGHT = 1400, 560

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)


flag = turtle.Turtle()

start=160
flag.penup()
flag.goto(0,50)
for i in range(2):
    for j in range (5):
        flag.penup()
        flag.forward(160)
        flag.dot()
        flag.penup()

    flag.goto(0, start)
    start = start + 50
turtle.done()

