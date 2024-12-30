def fun(x, y, z):
    return (x + y + z) / 3
a,b,c = map(int,input().split(","))
d = fun(a,b,c)
print('%.4f' % d)
