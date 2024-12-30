def sum(x):
    i=0
    s=0
    while (powers(x,i)/fac(i))>=1e-6:
        s=s+powers(x,i)/fac(i)
        i=i+1
    return s

def powers(x,n):
    p=1.0
    for i in range(1,n+1):
        p*=x
    return p

def fac(n):
    f=1
    for i in range(2,n+1):
        f=f*i
    return f

x=int(input("input x:"))
ex=sum(x)
print("%.2f powers of e =%.10f\n"%(x,ex))



