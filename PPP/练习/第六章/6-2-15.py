h = int(input())
N = int(input())
H = h
for i in range(1,N):
    h = h*0.5
    H = H + h*2
print("%.2f" % H)