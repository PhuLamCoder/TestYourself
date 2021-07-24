from time import sleep
#sleep(5)
for i in range(1,8):
    for j in range(1,8):
        if i < round(7/2) :
            if 4 <= j <= 3 + i :
                print('{0:<3}'.format('*'), end='')
            else:
                print('   ', end='')
        elif i == 4 :
            print('{0:<3}'.format('*'), end='')
        else :
            if 1 <= j <= 8 - i:
                print('{0:<3}'.format('*'), end='')
            else:
                print('   ', end='')
    print()
#sleep(5)
for i in range(1,8):
    for j in range(1,8):
        if i < round(7/2) :
            if i == 3 and j == 5 :
                print('   ', end='')
            elif 4 <= j <= 3 + i :
                print('{0:<3}'.format('*'), end='')
            else:
                print('   ', end='')
        elif i == 4 :
            print('{0:<3}'.format('*'), end='')
        else :
            if i == 5 and j == 2 :
                print('   ', end='')
            elif 1 <= j <= 8 - i:
                print('{0:<3}'.format('*'), end='')
            else:
                print('   ', end='')
    print()
#sleep(5)
for i in range(1,8):
    for j in range(1,8):
        if i <= 4 :
            if 4 <= j <= 8-i:
                print('{0:<3}'.format('*'), end ='')
            else:
                print('   ', end='')
        else:
            if 8-i <= j <= 4:
                print('{0:<3}'.format('*'), end='')
            else:
                print('   ', end='')
    print()
#sleep(5)
for i in range(1,8):
    for j in range(1,8):
        if i <= 4 :
            if i == 2 and j ==5 :
                print('   ', end='')
            elif 4 <= j <= 8-i:
                print('{0:<3}'.format('*'), end ='')
            else:
                print('   ', end='')
        else:
            if i == 6 and j == 3 :
                print('   ', end='')
            elif 8-i <= j <= 4:
                print('{0:<3}'.format('*'), end='')
            else:
                print('   ', end='')
    print()





