def flower(n):
    d = n
    a = 0
    while n > 0:
        c = (n%10)**3
        n = n//10
        a += c
    if a == d:
        print(a)
        return True
a = int(input())
flag = 0
for i in range(2,a+1):
    if flower(i):
        flag = 1
if flag == 0:
    print("none")