import turtle
#opens crosses fill and read lines
with open('crosses.txt') as f:
    lines = f.readlines()
print(lines)
#prints out names from txt file

#removes /n after all names
crossnames = [s.replace("\n", "") for s in lines]

print(crossnames)
#prints out new list



#Width and height for turtles
WIDTH, HEIGHT = 1400, 560

#Setting up where turtle starts
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  #sets up window
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT) #turtle boundires


flag = turtle.Turtle() #Naming turtle

start=200
flag.penup() #So turtle doesnt draw lines
flag.goto(0,100) #Tells turtle where to start
for i in range(2): #Loops twice so does 2 lines of dots
    for j in range (5): #Loops 5 times to do 5 dots
        flag.penup()
        flag.forward(160) #Move forward for dots
        flag.dot() #Places Dot
        flag.penup() #Puts dot back up

    flag.goto(0, start) #Tells turtle where to go for 2nd line
    start = start + 100 #Adds 100 so turtle goes higher

names = turtle.Turtle() #Name turtle
start=200 #Height Where turtle starts
number = 0
names.penup() #so doesn't do line
names.goto(0,50) #Start point
for i in range(2): #Repeates twice for both rows
    for j in range (5): # Repeats 5 for 5 names per row
        names.forward(160) #Spaces between names/dots
        names.write(crossnames[number]) #Sorts list so names are spread out
        number += 1

    names.goto(0, start) # Moves to 2nd line
    start = start + 50







turtle.done()

