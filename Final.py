import turtle
with open('crosses.txt') as f:
    lines = f.readlines()
print(lines)

new_list = [s.replace("\n", "") for s in lines]

print(new_list)

names = sorted(new_list)

print(names)


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

liz = turtle.Turtle()
start=160
number = 0
liz.penup()
liz.goto(0,50)
for i in range(2):
    for j in range (5):
        liz.forward(160)
        liz.write(names[number])
        number += 1




    liz.goto(0, start)
    start = start + 50






turtle.done()
