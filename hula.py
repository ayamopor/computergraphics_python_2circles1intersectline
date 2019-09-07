import turtle
#initialize input x1 y1 x2 y2 and r
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
r = int(input("r: "))

#point 1 coordinate is x1, y1. applies to point 2 as well
titik1 = (x1, y1)
titik2 = (x2, y2)

#screen initializtion
wn = turtle.Screen()
wn.bgcolor("black")
turtle = turtle.Turtle()
turtle.color("white")
turtle.speed(1)

#drawing the first circle
turtle._delay(30)
turtle.penup()
turtle.setposition(titik1)
turtle.setheading(turtle.towards(titik2))
turtle.pendown()
turtle.circle(-r)

#drawing the intersect line
turtle.penup()
turtle.goto(titik1)
turtle.pendown()
turtle._delay(30)
turtle.goto(titik2)

#drawing the second circle
turtle._delay(30)
turtle.penup()
turtle.setposition(titik2)
turtle.pendown()
turtle.circle(r)

#screen waits for the user
wn.exitonclick()