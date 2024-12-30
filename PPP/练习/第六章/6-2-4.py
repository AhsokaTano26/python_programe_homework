def f(x):
    b = x
    if b < 20:
        a = 6*(x**2)+1
    elif b < 40:
        a = (3*x-60)**0.5
    else:
        a = 100/(x+1)
    return a
a = float(input())
c = f(a)
print("%.2f" % c)
