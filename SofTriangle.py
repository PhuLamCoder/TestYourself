from math import sqrt
a, b, c = map(float, input('Nhập lần lượt 3 cạnh a, b, c > 0 của tam giác : ').split())
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print('Cạnh của tam giác không hợp lệ')
    exit()
p = (a + b + c)/2
S = sqrt(p*(p-a)*(p-b)*(p-c))
print('Diện tích của tam giác đó là : ',S)
