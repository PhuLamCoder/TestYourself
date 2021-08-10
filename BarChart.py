from turtle import *

setworldcoordinates(-1, -2, 70, 60)
speed(0)
hideturtle()

gioi = numinput(title='Nhập số liệu', prompt='Giỏi :', minval=0, maxval=50)
kha = numinput(title='Nhập số liệu', prompt='Khá :', minval=0, maxval=50-gioi)
tb = numinput(title='Nhập số liệu', prompt='Trung Bình :', minval=0, maxval=50-gioi-kha)
yeu = 50 - gioi - kha - tb

up()
goto(-1, -0.5); write('0', align='center', font=('tahoma', 12, 'normal'))
goto(-1, 4.5); write('5', align='center', font=('tahoma', 12, 'normal'))
goto(0, 0)
down()

goto(0, 55)
up(); goto(-0.5, 5); down(); goto(0.5, 5)
up(); goto(-0.5, 10); down(); goto(0.5, 10)
up(); goto(-0.5, 15); down(); goto(0.5, 15)
up(); goto(-0.5, 20); down(); goto(0.5, 20)
up(); goto(-0.5, 25); down(); goto(0.5, 25)
up(); goto(-0.5, 30); down(); goto(0.5, 30)
up(); goto(-0.5, 35); down(); goto(0.5, 35)
up(); goto(-0.5, 40); down(); goto(0.5, 40)
up(); goto(-0.5, 45); down(); goto(0.5, 45)
up(); goto(-0.5, 50); down(); goto(0.5, 50)
up(); goto(-0.5, 53); down(); goto(0, 55); goto(0.5, 53)

up(); goto(5, 52); write('Số lượng', align='center', font=('tahoma', 12, 'normal')); goto(0, 0); down()
goto(65 , 0)

fillcolor("#006633")
begin_fill()
goto(5, 0); goto(5, gioi); goto(7.5, gioi); write(gioi, align='center', font=('tahoma', 12, 'normal'))
goto(10, gioi); goto(10, 0)
end_fill()
up(); goto(7.5, -2); write('Giỏi', align='center', font=('tahoma', 12, 'normal')); goto(15, 0); down()

fillcolor("#FF9900")
begin_fill()
goto(15, kha); goto(17.5, kha); write(kha, align='center', font=('tahoma', 12, 'normal'))
goto(20, kha); goto(20, 0)
end_fill()
up(); goto(17.5, -2); write('Khá', align='center', font=('tahoma', 12, 'normal')); goto(25, 0); down()

fillcolor("#660099")
begin_fill()
goto(25, tb); goto(27.5, tb); write(tb, align='center', font=('tahoma', 12, 'normal'))
goto(30, tb); goto(30, 0)
end_fill()
up(); goto(27.5, -2); write('TB', align='center', font=('tahoma', 12, 'normal')); goto(35, 0); down()

fillcolor("#33CCFF")
begin_fill()
goto(35, yeu); goto(37.5, yeu); write(yeu, align='center', font=('tahoma', 12, 'normal'))
goto(40, yeu); goto(40, 0)
end_fill()
up(); goto(37.5, -2); write('Yếu', align='center', font=('tahoma', 12, 'normal')); goto(45, 0); down()

mainloop()