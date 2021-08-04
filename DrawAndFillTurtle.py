from turtle import *
color("#B31535")
begin_fill()
forward(150); left(90); forward(150); left(90); forward(150); left(90); forward(150); left(90)
end_fill()

color("#3ACCD7")
begin_fill()
circle(150, 90); left(90); circle(150, 90); up(); back(150); down(); circle(150, 90); left(90); circle(150, 90)
end_fill()

left(90); up(); circle(150, 30); down()
color("#B31535")
begin_fill()
circle(150, 30)
left(60)
circle(150, 30)
left(60)
circle(150, 30)
left(60)
circle(150, 30)
end_fill()



mainloop()