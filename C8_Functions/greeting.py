# <Python编程基础及应用> 随书代码 高等教育出版社
#greeting.py
def greeting(name,gender):
    name = name.title()
    s = "Mr" if gender=='male' else 'Miss'
    print("Hi,",s,name)

greeting("henry",'male')