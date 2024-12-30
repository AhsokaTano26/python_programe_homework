import math
a = input("长(cm):")
b = input("宽(cm):")
a = float(a)
b = float(b)
d = math.sqrt(pow(a,2)+pow(b,2))
print("对角度长度为:%.1fcm." % d)

