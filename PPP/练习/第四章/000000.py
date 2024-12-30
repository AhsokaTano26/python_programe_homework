A = eval(input())
C = A[:]
a = 0
for i in C:
    if i == 0:
        A.remove(0)
        a = a+1
while a != 0:
    A.append(0)
    a = a - 1
print(A)
