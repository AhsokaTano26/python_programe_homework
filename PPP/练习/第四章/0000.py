A = eval(input())
A = list(A)
n,m = map(int,input().split(","))
c = len(A)
if n > c:
    print("error")
else:
    b = A[n]
    i = 1
    while i <= m:
        A.append(b)
        i = i + 1
    print(A)