import math
R1 = float(input())
R2 = float(input())
r1 = R1/2
r2 = R2/2
def VV(R):
    a = math.pi
    V = (4/3)*a*(R**3)
    return V
V = VV(r1)+VV(r2)
r = math.pow(V,1/3)
print("正方体边长为:%.2f." % r)