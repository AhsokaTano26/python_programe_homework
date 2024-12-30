A = eval(input())
A.reverse()
res = []
for i in A:
    if i not in res:
        res.append(i)
res.reverse()
print(res)
