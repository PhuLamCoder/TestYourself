from turtle import *

speed(0)
width(2)

fillcolor("#006633")
begin_fill()
forward(150); write('10%', align='center', font=('tahoma', 20, 'normal')); forward(50); left(90)
circle(200, 18); write('Giỏi', align='left', font=('tahoma', 20, 'normal')); circle(200, 18)
end_fill()

x = pos(); goto(0, 0)

fillcolor("#FF9900")
begin_fill()
goto(x)
circle(200, 108); write('Khá', align='right', font=('tahoma', 20, 'normal')); circle(200, 108)
end_fill()

y = pos(); goto(0, 0)

fillcolor("#660099")
begin_fill()
goto(y); circle(200, 36); write('20%', align='right', font=('tahoma', 20, 'normal')); circle(200, 36)
end_fill()

z = pos(); goto(0, 0)

fillcolor("#33CCFF")
begin_fill()
goto(z); circle(200, 18);  write('10%', align='right', font=('tahoma', 20, 'normal')); circle(200, 18)
end_fill()

up()
goto(200, -75);  write('Yếu', align='left', font=('tahoma', 20, 'normal'))
goto(50, -225);  write('TB', align='left', font=('tahoma', 20, 'normal'))
goto(-175, 50);  write('60%', align='left', font=('tahoma', 20, 'normal'))

mainloop()