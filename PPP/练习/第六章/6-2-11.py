a = list(input())
b = []
for i in a:
    i = int(i)
    i = (i + 5) % 10
    i = str(i)
    b.append(i)
c = b[:]
for i in range(0,len(c)):
    c[-i-1] = b[i]
print("".join(c))