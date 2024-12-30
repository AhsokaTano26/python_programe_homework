A = eval(input())
A = list(A)
total = len(A)
b = sum(A)
e = b/total
c = int(b%total)
if c == 0:
    print(int(e))
else:
    print("%.2f" % e)
