import math
r = eval(input("请输入圆的半径:"))
fArea = math.pi * r * r
fPerimeter = 2*r*math.pi
print("周长:{:.2f},面积:{:.3f}".format(fPerimeter,fArea))
