a = int(input())
b = int(input())
if a <= 0 or b <= 0:
    print("illegal data")
elif a == b and a > 0 and b > 0:
    print("It's a square")
else:
    print("It's a rectangle")