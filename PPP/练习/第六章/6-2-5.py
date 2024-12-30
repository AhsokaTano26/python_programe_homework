a = int(input())
m1 = [3,4,5]
m2 = [6,7,8]
m3 = [9,10,11]
m4 = [12,1,2]
if a >= 1 and a <= 12:
    if a in m1:
        b = "spring"
    elif a in m2:
        b = "summer"
    elif a in m3:
        b = "autumn"
    else:
        b = "winter"
else:
    b = "error"
print(b)