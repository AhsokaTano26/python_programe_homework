def classify(x, ls):
    a = []
    b = []
    for i in ls:
        if x < i:
            a.append(i)
        else:
            b.append(i)
    dic["k1"] = a
    dic["k2"] = b
x = int(input())
ls = input().split()
ls = list(map(int, ls))  # map函数使用说明：int函数作用于ls中每一个元素，返回一个新的整数序列，再用list转换成列表
dic = {}
classify(x, ls)
print(sorted(list(dic.items())))