A = eval(input())
C = A[:]
B = sorted(A)
a = B[0]
b = B[-1]
for i in C:
    if i == a:
        A.remove(a)
if len(A) == 0:
    print(A)
else:
    for i in C:
        if i == b:
            A.remove(b)
    print(A)

