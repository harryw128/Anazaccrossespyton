import turtle

liznewton = turtle.Turtle()
turtle.tracer()
H = 3
W = 5
S = 15


def square(side):
    for i in range(4):
        liznewton.forward(side)
        liznewton.left(90)


def row(n, side):
    for i in range(n):
        square(side)
        liznewton.forward(side)
    liznewton.penup()
    liznewton.left(180)
    liznewton.forward(n * side)
    liznewton.left(180)
    liznewton.pendown()


def row_of_rows(m, n, side):
    for i in range(m):
        row(n, side)
        liznewton.penup()
        liznewton.left(90)
        liznewton.forward(side)
        liznewton.right(90)
        liznewton.pendown()
    liznewton.penup()
    liznewton.right(90)
    liznewton.forward(m * side)
    liznewton.left(90)
    liznewton.pendown()


row_of_rows(H, W, S)
