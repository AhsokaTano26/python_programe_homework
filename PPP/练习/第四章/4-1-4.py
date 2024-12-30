def Fibonacci(num,n):
    for i in range(2,n+2,1):
        a = num[i-1] + num[i-2]
        num.append(a)
    return num[n-1]
num = [1,1]
n = int(input())
print(Fibonacci(num,n))