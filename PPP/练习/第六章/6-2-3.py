def jo(x):
    if x % 2 == 0:
        return 1
a = int(input())
s0 = [0]
s1 = [y for y in range(1,11,1)]
s2 = [x for x in range(11,19,1)]
s3 = [x for x in range(19,29,1)]
s4 = [x for x in range(29,37,1)]
if a >= 0 and a <= 36:
    if a in s0:
        b = "green"
    elif a in s1:
        if jo(a) == 1:
            b = "black"
        else:
            b = "red"
    elif a in s2:
        if jo(a) != 1:
            b = "black"
        else:
            b = "red"
    elif a in s3:
        if jo(a) == 1:
            b = "black"
        else:
            b = "red"
    elif a in s4:
        if jo(a) != 1:
            b = "black"
        else:
            b = "red"
else:
    b = "error"
print(b)