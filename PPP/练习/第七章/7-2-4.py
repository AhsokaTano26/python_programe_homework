a = list(map(str, input().split()))
b = {}
for x in a:
    b[x] = a.count(x)
c = max(b.values())
d = {}
for x in b:
    if b[x] == c:
        d[x] = c
d = sorted(d.items())
d = dict(d)
for k,v in d.items():
    print(k,v)
#key=lambda e:e[0]