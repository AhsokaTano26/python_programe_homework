# <Python编程基础及应用> 随书代码 高等教育出版社
#simplegrr.py
g1 = [x**2 for x in range(1,10,2)]
g2 = (x**2 for x in range(1,10,2))
print(type(g1),g1)
print(type(g2),list(g2))