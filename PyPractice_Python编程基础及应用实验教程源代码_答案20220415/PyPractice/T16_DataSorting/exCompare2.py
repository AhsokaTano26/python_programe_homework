#exCompare2.py
a = ("Python", 1, 2, 3, 4)
b = ("Python", 2, 3, 1)
c = ["Python", 100, 200, 300]
d = ["c++", 1, 2, 3]
e = ["c++", 1, 2, 3]
print('元组比较-a大于b：',a > b)
print('元组比较-a小于b：',a < b)
print('列表比较-c小于d：',c < d)
print('列表比较-c大于等于d：',c >= d)
print('列表比较-d等于e：',d == e)