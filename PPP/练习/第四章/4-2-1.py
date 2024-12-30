A = eval(input())
A = list(A)
A.sort(reverse=True)
output = ''.join(str(i) for i in A)
output = int(output)
print(output)

