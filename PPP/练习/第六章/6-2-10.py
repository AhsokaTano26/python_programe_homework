def ss(a):
    for i in range(2,a):
        if a % i == 0:
            return 0
def hw(a):
    a = str(a)
    a = list(a)
    b = len(a)
    for i in range(0,b//2):
        if a[i] == a[-i-1]:
            return 1
n = float(input())
c = []
if n < 1:
    print("illegal input")
elif n % 1 != 0:
    print("illegal input")
else:
    n = int(n)
    for i in range(2,n):
        if i < 10:
            if ss(i) != 0:
                i = str(i)
                c.append(i)
        else:
            if ss(i) != 0 and hw(i) == 1:
                i = str(i)
                c.append(i)
print(" ".join(c))