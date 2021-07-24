from random import randrange
while True :
    print('Welcom to guess game!')
    x = randrange(1, 101)
    print("Máy đã ra số từ 1 đến 100!, bạn có 7 lượt đoán!")
    time = 1
    while True :
        if time == 8 :
            print('Mày xui lắm con chai hahaha! Số', x, " cơ!")
            break
        print('Lần thứ ', time, '!')
        guess = int(input("Mời bạn đoán số : "))
        if guess < x :
            print("Lớn hơn cơ, lại đy!")
            time +=1
        elif guess > x :
            print("Bé hơn cơ, lại đy!")
            time += 1
        else :
            print('Bingo! Hay quá! Số ',x ,'đúng rồi ditmemay!')
            break
    if input("có chơi tiếp không mạy? c/k : ") == 'k' :
        print("Thank for playing!")
        break