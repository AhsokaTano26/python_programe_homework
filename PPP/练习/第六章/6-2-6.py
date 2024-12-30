n,m = map(int,input().split())
if type(n) != int or type(m) != int:
    print("illegal input")
elif m < 0 or n < 0:
    print("illegal input")
elif m - n <= 2:
    print("illegal input")
elif n >= 10 or m >= 10:
    print("illegal input")
else:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i != j and i != k and j != k and i != 0:
                    print(i,j,k,sep='',end=' ')