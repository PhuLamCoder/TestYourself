from turtle import *
hideturtle()
tracer(False)

color('yellow')
begin_fill()
forward(50); circle(20, 90); forward(20); right(90); forward(20); circle(-20, 90); forward(40)
circle(-20, 90); forward(60); circle(3, 180); forward(50); right(90); forward(10)
circle(-20, 90); forward(60); circle(-20, 90); forward(36); circle(-20, 90)
end_fill()

color('white')
up(); goto(60, -55); begin_fill(); circle(-5); end_fill(); goto(45, 5); setheading(180); down()

color('blue')
begin_fill()
forward(50); circle(20, 90); forward(20); right(90); forward(20); circle(-20, 90); forward(40)
circle(-20, 90); forward(60); circle(3, 180); forward(50); right(90); forward(10)
circle(-20, 90); forward(60); circle(-20, 90); forward(36); circle(-20, 90)
end_fill()

color('white')
up(); goto(-15, 60); begin_fill(); circle(-5); end_fill()

update()
mainloop()