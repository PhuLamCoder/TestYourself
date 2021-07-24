chuoi = input('Mời nhập chuỗi danh từ : ')
chuoi = chuoi.split()
sochu = len(chuoi)
rename = ''
for i in chuoi :
    for j in range(0, len(i)) :
        if j == 0 :
            rename = rename + i[0].upper()
        else:
            rename = rename + i[j].lower()
    rename = rename + ' '
print('Sau khi sửa :',rename)

