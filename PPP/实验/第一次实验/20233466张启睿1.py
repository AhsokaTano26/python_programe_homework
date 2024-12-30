def prime(a):
    for i in range(2,a):
        if a % i == 0:
            return 0
num = int(input())
for i in range(2,int(num/2) + 1):
    if prime(i) != 0:
        if prime(num-i) != 0:
            print(num,"=",i,"+",num-i)
            break