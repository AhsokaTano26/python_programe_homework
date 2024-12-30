a = eval(input())
ls = [x for x in range(1,a+1,1)]
ls1 = []
for i in range(1,a):
    ls1.append(ls[i])
ls1.append(1)
print(ls1)