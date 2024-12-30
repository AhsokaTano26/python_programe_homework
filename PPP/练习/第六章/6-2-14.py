a = str(input())
b = list(a)
for i in range(0,26):
    if chr(ord("a") + i) in b:
        c = b.count(chr(ord("a") + i))
        d = str(chr(ord("a") + i))
        print(d,c,sep=',')  #"%s,%d" % (d, c)