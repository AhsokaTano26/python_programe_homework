N = eval(input())

guoPower,wangPower = 100,100
for x in range(N):
    guoPower *= 1.001
    if x % 5 in [0,1,2]:
        wangPower *= 1.002
    else:
        wangPower *= 0.999

print(f"{guoPower:.5f},{wangPower:.5f}")
