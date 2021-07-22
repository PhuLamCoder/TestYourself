# Nhập 1 list có N số ngẫu nhiên không trùng
from random import randrange
N = int(input('Mời bạn nhập số phần tử của mảng : '))
lst = []
for i in range(N) :
    x = randrange(1,21)
    while lst.count(x) == 1 :
        x = randrange(1, 21)
    lst.append(x)
print(lst)


