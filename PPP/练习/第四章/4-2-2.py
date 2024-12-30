ls = eval(input())
ls2 = []
for x in ls:
    if ls.count(x) == 1:
        ls2.append(x)
ls2.sort()
if len(ls2) == 0:
    print(False)
else:
    ls2 = list(ls2)
    out = ",".join(str(i) for i in ls2)
    print(out)
