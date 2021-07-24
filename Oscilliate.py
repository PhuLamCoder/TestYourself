def oscilliate(x, y) :
    chuoi = '',
    for i in range(x, y):
        chuoi = chuoi + (i, -i,)
    return chuoi
for n in oscilliate(-3,5):
    print(n, end=' ')
print()