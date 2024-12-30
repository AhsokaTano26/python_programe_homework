ls = eval(input())
n = eval(input())
#  重复列表元素n次
ls2 = []
a = 0
for i in ls:
    while a < 5:
        ls2.append(i)
        a = a+1
    else:
        a = a-5
ls3 = [x*x  for  x  in  ls2]
#  下面代码去除重复元素
ls4=[]
for x in ls3:
    if ls3.count(x) > 1 and x not in ls4:
        ls4.append(x)
print(ls4)