from random import randrange
def creatematrix(M, N) :
    lst = []
    for i in range(M) :
        cul = []
        for j in range(N) :
            cul.append(randrange(-10,11))
        lst.append(cul)
    return lst
def printmatrix(lst) :
    for row in lst :
        for ele in row :
            print('{0:>3}'.format(ele), end = '   ')
        print()
def printaline(lst, row, N) :
    for i in range(N) :
        print(lst[row][i], end = '  ')
def printaculumn(lst, culumn, M) :
    for i in range(M) :
        print('{0:>3}'.format(lst[i][culumn]))
M = int(input('Nhập số dòng của matrix : '))
N = int(input('Nhập số cột của matrix : '))
lst = creatematrix(M,N)
printmatrix(lst)
print('Nhập dòng bất kì muốn xuất từ 0 ->',M-1 ,':', end=' ')
row = int(input())
printaline(lst, row, N)
print()
print('Nhập cột bất kì muốn xuất từ 0 ->',N-1 ,':', end=' ')
culumn = int(input())
printaculumn(lst, culumn, M)
print('-'*50)
MAX = 0
for row in lst :
    for ele in row :
        if ele > MAX :
            MAX = ele
print('Số MAX trong matrix là :',MAX)