import turtle  #1. import modules
import random

#Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor('lightgreen')

Bob = turtle.Turtle()  # 3.  Create two turtles
Jimmy = turtle.Turtle()
Bob.color('orange')
Jimmy.color('blue')
Bob.shape('turtle')
Jimmy.shape('turtle')
Jimmy.speed(1)
Bob.speed(1)

Bob.up()  # 4.  Pick up the pen so we don’t get lines
Jimmy.up()
Bob.goto(-100, 20)
Jimmy.goto(-100, -20)

## 5. your code goes here
x = random.randrange(1, 100)
Jimmy.forward(x)
Bob.forward(x)
Bob.goto(-100, 20)
Jimmy.goto(-100,-20)

rdist = random.randrange(0,10)

for i in range(10): 
  Jimmy.forward(rdist)
  Bob.forward(rdist)

Jimmy.goto(-100,-20)
Bob.goto(-100,20)

# Part B - complete part B here
Bob.pendown()
for sides in [3,4,6,9,12]:
    for i in range(sides):
     Bob.forward(50)
     Bob.left(360/sides)
    Bob.clear()

window.exitonclick()