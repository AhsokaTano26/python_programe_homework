import random

iNumber = 97
iCounter = 0
while True:
    i = int(input("我的数字你来猜(1~1000):"))
    iCounter += 1
    if i > iNumber:
        print("猜大了")
    elif i < iNumber:
        print("猜小了")
    else:
        print("恭喜你，猜对了!")
        break

print("此轮猜数次数:",iCounter)