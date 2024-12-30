
a = input().split(',')
a = list(a)
b = eval(input())
m = []
for x in range(len(a)):
    n = []
    n.append(a[x])
    n.append(b[x])
    m.append(n)
m = dict(m)
m = sorted(m.items(),key=lambda a:a[1])
m = list(m)
for x in range(len(m)):
    m[x] = list(m[x])
print(m)