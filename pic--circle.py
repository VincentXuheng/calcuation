#不断画圆圈
import turtle as t
t.speed('fast')
t.hideturtle()
t.bgcolor('black')

i=0
while i<135:
    t.pencolor('red')
    t.penup()
    t.goto(0,0)
    t.forward(100)
    t.pendown()
    t.circle(50)
    t.left(5)
    i+=1







