n = int(input())
a = 2
b = 1
c = 3
d = 2
e = 0
if n == 1:
    e = 2
elif n == 2:
    e = 3.5
else:
    e = 3.5
    for i in range(1,n-1):
        c = a + c
        a = c - a
        d = d + b
        b = d - b
        e = e + (c/d)
print("%.4f" % e)