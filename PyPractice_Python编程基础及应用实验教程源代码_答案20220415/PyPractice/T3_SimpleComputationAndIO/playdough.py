import math
d1 = eval(input("请输入球1的直径:"))
d2 = eval(input("请输入球2的直径:"))
r1 = d1/2
r2 = d2/2
V1 = 4*math.pi*(r1**3)/3
V2 = 4*math.pi*(r2**3)/3
V = V1 + V2
L = V**(1/3)
print(f"正方体边长为:{L:.2f}.")