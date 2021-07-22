from random import randrange
m = int(input('Nhập số hàng của ma trận : '))
n = int(input('Nhập số cột của ma trận : '))
agay = []
for i in range(m) :
    col = []
    for j in range(n) :
        col.append(randrange(-10, 11))
    agay.append(col)
print(agay)
newa = []
for i in range(n) :
    col = []
    for j in range(m) :
        col.append(agay[j][i])
    newa.append(col)
print(newa)
