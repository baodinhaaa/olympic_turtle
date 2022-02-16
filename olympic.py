import turtle
import math

# object tr for turtle
turtle.Screen().setup(450, 350)
tr = turtle.Turtle()
# screen = turtle.Screen()
# set thikness for each ring

# tr.speed(1)
tr.shape('turtle') #'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
# tr.color("red", "blue")
# tr.left(45)
# tr.setheading(-90)

tr.pen(resizemode='auto', shearfactor=10)
def mycircle(center, radius, angle):
    pos=center
    pos[0] = center[0]*math.cos(angle)
    pos[1] = center[1]*math.sin(angle)
    tr.penup()
    tr.goto(pos)
    tr.pendown()
    tr.setheading(angle)
    tr.circle(radius,None,None)
def OlympicCircle(color, center, mask, radius, angle=0):
    # center[1] -= radius
    tr.color("white")
    tr.pensize(20)
    tr.speed(12)
    tr.penup()
    tr.hideturtle()
    tr.goto(center)
    tr.pendown()
    tr.circle(radius)

    tr.color(color, "orange")
    tr.pensize(12)
    tr.speed(10)
    tr.showturtle()
    # mycircle(center, radius, angle)
    tr.penup()
    tr.goto(center)
    tr.pendown()
    tr.setheading(angle)
    tr.circle(radius,None,None)
k = 5
OlympicCircle("blue", [-65*2-2*k, 0], None, 60, 0)
# OlympicCircle("yellow", [-65*2-2*k, 0], None, 60, -90)
OlympicCircle("yellow", [-32.5*2-k, -30*2], None, 60)
OlympicCircle("black", [0, 0], None, 60)
OlympicCircle("green", [32.5*2+k, -30*2], None, 60)
OlympicCircle("red", [65*2+2*k, 0], None, 60)

# tr.penup()
# tr.home()
tr.hideturtle()
turtle.done()