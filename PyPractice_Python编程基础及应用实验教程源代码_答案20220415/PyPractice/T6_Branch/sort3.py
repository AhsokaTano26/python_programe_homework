a,b,c  = eval(input())
if a<=b:
    if b<=c:
        print(f"{a},{b},{c}")
    else:
        if a<=c:
            print(f"{a},{c},{b}")
        else:
            print(f"{c},{a},{b}")
else:
    if a<=c:
        print(f"{b},{a},{c}")
    else:
        if b<=c:
            print(f"{b},{c},{a}")
        else:
            print(f"{c},{b},{a}")
        



