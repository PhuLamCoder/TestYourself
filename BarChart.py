from turtle import *

setworldcoordinates(-1, -5, 60, 40)
speed(0)
hideturtle()

up()
goto(-1, -0.5); write('0', align='center', font=('tahoma', 12, 'normal'))
goto(-1, 4.5); write('5', align='center', font=('tahoma', 12, 'normal'))
goto(0, 0)
down()

goto(0, 37)
up(); goto(-0.5, 5); down(); goto(0.5, 5)
up(); goto(-0.5, 10); down(); goto(0.5, 10)
up(); goto(-0.5, 15); down(); goto(0.5, 15)
up(); goto(-0.5, 20); down(); goto(0.5, 20)
up(); goto(-0.5, 25); down(); goto(0.5, 25)
up(); goto(-0.5, 30); down(); goto(0.5, 30)
up(); goto(-0.5, 35); down(); goto(0, 37); goto(0.5, 35)

up(); goto(7.5, 35); write('Số lượng', align='center', font=('tahoma', 12, 'normal')); goto(0, 0); down()
goto(60, 0)

fillcolor("#006633")
begin_fill()
goto(5, 0); goto(5, 5); goto(7.5, 5); write('5', align='center', font=('tahoma', 12, 'normal'))
goto(10, 5); goto(10, 0)
end_fill()
up(); goto(7.5, -2); write('Giỏi', align='center', font=('tahoma', 12, 'normal')); goto(15, 0); down()

fillcolor("#FF9900")
begin_fill()
goto(15, 30); goto(17.5, 30); write('30', align='center', font=('tahoma', 12, 'normal'))
goto(20, 30); goto(20, 0)
end_fill()
up(); goto(17.5, -2); write('Khá', align='center', font=('tahoma', 12, 'normal')); goto(25, 0); down()

fillcolor("#660099")
begin_fill()
goto(25, 10); goto(27.5, 10); write('10', align='center', font=('tahoma', 12, 'normal'))
goto(30, 10); goto(30, 0)
end_fill()
up(); goto(27.5, -2); write('TB', align='center', font=('tahoma', 12, 'normal')); goto(35, 0); down()

fillcolor("#33CCFF")
begin_fill()
goto(35, 5); goto(37.5, 5); write('5', align='center', font=('tahoma', 12, 'normal'))
goto(40, 5); goto(40, 0)
end_fill()
up(); goto(37.5, -2); write('Yếu', align='center', font=('tahoma', 12, 'normal')); goto(45, 0); down()

mainloop()