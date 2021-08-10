from turtle import *
ht()
speed(0)
width(2)
gioi = numinput(title='Nhập số liệu', prompt='Giỏi :', minval=0, maxval=50)
kha = numinput(title='Nhập số liệu', prompt='Khá :', minval=0, maxval=50-gioi)
tb = numinput(title='Nhập số liệu', prompt='Trung Bình :', minval=0, maxval=50-gioi-kha)
yeu = 50 - gioi - kha - tb

tlgioi = gioi*360/50
tlkha = kha*360/50
tltb = tb*360/50
tlyeu = yeu*360/50

fillcolor("#006633")
begin_fill()
forward(200); left(90)
circle(200, tlgioi)
end_fill()

x = pos(); goto(0, 0)

fillcolor("#FF9900")
begin_fill()
goto(x)
circle(200, tlkha)
end_fill()

y = pos(); goto(0, 0)

fillcolor("#660099")
begin_fill()
goto(y); circle(200, tltb)
end_fill()

z = pos(); goto(0, 0)

fillcolor("#33CCFF")
begin_fill()
goto(z); circle(200, tlyeu)
end_fill()

up()
if tlgioi > 0 :
    setheading(0)
    goto(0, 0); left(tlgioi/2); forward(100); write(f'{gioi*2:.2f}%', align='center', font=('tahoma', 12, 'normal'))
    forward(115); write('Giỏi', align='center', font=('tahoma', 12, 'normal'))
if tlkha > 0 :
    setheading(0)
    goto(0, 0); left(tlgioi + tlkha/2); forward(100); write(f'{kha*2:.2f}%', align='center', font=('tahoma', 12, 'normal'))
    forward(115); write('Khá', align='center', font=('tahoma', 12, 'normal'))
if tltb > 0 :
    setheading(0)
    goto(0, 0); left(tlgioi + tlkha + tltb/2); forward(100); write(f'{tb*2:.2f}%', align='center', font=('tahoma', 12, 'normal'))
    forward(115); write('TB', align='center', font=('tahoma', 12, 'normal'))
if tlgioi > 0 :
    setheading(0)
    goto(0, 0); right(tlyeu/2); forward(100); write(f'{yeu*2:.2f}%', align='center', font=('tahoma', 12, 'normal'))
    forward(115); write('Yếu', align='center', font=('tahoma', 12, 'normal'))
mainloop()