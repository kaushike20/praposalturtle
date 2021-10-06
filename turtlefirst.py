import turtle
import time
s=turtle.Screen().bgcolor("black")
t=turtle.Turtle()
t.speed(0)
t.width(12)

def curve():
    for i in range(0,200):
        t.right(1)
        t.forward(1)

def main():
    t.color('red','red')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

main()
t.penup()
t.goto(-280,-20)
t.pencolor('blue')
t.write("I  YOU",align='left',font=("courier",150,'bold italic'))

time.sleep(13)
