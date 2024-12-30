a = input()
n = 0
b = []
c = []
def m(a):
    import re
    return bool(re.search(r'\d',a))
if m(a) == True:
    for x in range(len(a)):
        if a[x].isnumeric():
            b.append(a[x])
            d = b.copy()
            c.append(d)
            if len(b)>n:
                n = len(b)
        else:
            b.clear()
    c.sort(key=len)
    print(''.join(c[-1]))
else:
    print('No digits')