N = int(input('Nhập số phần tử của list : '))
list = [0]*N
for i in range(N) :
    print('Mời bạn nhập phần tử thứ',i, ':', end =' ')
    list[i] = int(input())
    if i >= 1 :
        while list[i] < list[i-1] :
            print('Mời bạn nhập lại phần tử thứ', i, ':', end=' ')
            list[i] = int(input())
print(list)
