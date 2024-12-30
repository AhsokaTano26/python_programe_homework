import definite as df
def f1(x):
    return 1+x
def f2(x):
    return 1/(1+4*x*x)

n=int(input("请输入等分数:"))
y1=df.collect(f1,0,2,n)
y2=df.collect(f2,-1,1,n)
print("The definite integral of f1 is {:.6f}".format(y1))
print("The definite integral of f2 is {:.6f}".format(y2))