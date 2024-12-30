def myprint1(n):
    if n // 10 == 0:  #基例
        print(n,end = ' ')
    else:            #链条
        print(n % 10, end = ' ')
        myprint1(n // 10)

def myprint2(n):     #基例
    if n // 10 == 0:
        print(n,end = ' ')
    else:           #链条
        myprint2(n // 10)
        print(n % 10, end = ' ')
        
myprint1(345)
print()
myprint2(345)
