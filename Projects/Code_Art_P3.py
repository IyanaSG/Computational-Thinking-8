
# Start
import turtle 

t = turtle.Turtle()

turtle.Screen () .bgcolor ("Black")

# Rotating shape
t.color("yellow")
t.penup ()
t.goto(-100,100)
t.pendown ()
t.speed (10)
for i in range (200):
    t.forward (100 + i)
    t.left (90 + 1)

# Growing Shape
t.color("red")
t.penup ()
t.goto(100,-100)
t.pendown ()
t.speed (10)
for i in range (200):
    t.forward (100 + i)
    t.left (90 + 1)

# End
turtle.exitonclick ()