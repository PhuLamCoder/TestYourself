from math import sqrt
number = int(input('Nhập số căn cần tính (n > 0) : '))
if number <= 0 :
    print('Nhập số căn không hợp lệ!')
else :
    s = 0
    for i in range(1, number +1) :
        s = sqrt(2 + s)
    print('S(',number,') căn là : ',s)

