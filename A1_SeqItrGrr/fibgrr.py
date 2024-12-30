# <Python编程基础及应用> 随书代码 高等教育出版社
def FibonacciGenerator(n):
    assert n > 2   #为代码简单，作者要求n>2
    print(1,end=",")
    print(1,end=",")
    a = b = 1
    for i in range(3,n+1):
        c = a + b
        a,b = b,c
        print(c,end=",")

FibonacciGenerator(10)