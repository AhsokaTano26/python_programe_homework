a,b,c,d = input().split()
b,c,d = int(b),int(c),int(d)
avg = (b+c+d) / 3
stu = {"name":a,"english":b,"python":c,"math":d,"avg":avg}
e = [b,c,d]
e.sort(reverse=True)
print(stu["name"],end=" ")
for y in range(len(e)):
    print(f'{e[y]:.2f}',end=" ")
print("%.2f" % stu["avg"])