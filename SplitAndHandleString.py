chuoi = '5;7;8;-2;8;11;-13;9;10'
chuoi = chuoi.split(';')
for i in chuoi :
    print(i.rjust(2))
dem = 0
for i in chuoi :
    if int(i) % 2 == 0 :
        dem +=1
print('Số chữ số chẵn là :',dem)
dem = 0
for i in chuoi :
    if int(i) < 0 :
        dem += 1
print('Số chữ số âm là :',dem)
dem = 0
for i in chuoi :
    uoc = 0
    for j in range(1,int(i)+1):
        if int(i) % j == 0 :
            uoc +=1
    if int(i) > 0 and uoc == 2 :
        dem +=1
print('Số chữ số nguyên tố là :',dem)
tong = 0
for i in chuoi :
    tong += int(i)
print('Trung bình các số là :',tong/len(chuoi))




