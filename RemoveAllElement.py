from random import randrange
n = int(input('Nhập số phần tử của list : '))
list = [0]*n
for i in range(n) :
    list[i] = randrange(-5, 6)
print(list)
print('-'*30)
value = int(input('Hãy nhập giá trị bạn muốn xóa : '))
while list.count(value) > 0 :
    list.remove(value)
print('CHuỗi sau khi xóa : ')
print(list)