def optimize(chuoi):
    chuoi = chuoi.split()
    chuoi = ' '.join(chuoi)
    return chuoi
while True :
    chuoi = input('Nhập chuỗi : ')
    chuoi = optimize(chuoi)
    print('Chuỗi sau khi tối ưu :',chuoi)
    if input('Tiếp? c/k : ') == 'k':
        break
print('Byeee!!!')






