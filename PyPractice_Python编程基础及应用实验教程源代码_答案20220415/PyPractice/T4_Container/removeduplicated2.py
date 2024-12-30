v = list(eval(input("input:")))
print("before:",v)

v2 = v[:]
for x in v2:
    cnt = v.count(x)
    if cnt >= 2:
        for i in range(cnt-1):
            v.remove(x)

print("after:",v)


"""
作者说明：上述程序并不能完美地完全任务！
测试输入：1,7,6,7,7,True,'a',9.8,'a',True

如果列表中同时包括1和True, 或同时包括0和False，将会产生意料之外的结果！
原因在于：count(), remove(),index()等函数将1和True等同视之，将0和False等同视之！
下述代码的执行结果有助于说明问题。
v = [1,True,2,True,0,False]
print("count of 1:", v.count(1), ",count of True:", v.count(True))
print("count of 0:", v.count(0), ",count of False:", v.count(False))
print("index of True:",v.index(True), ",index of False",v.index(False))
v.remove(True)
print("after v.remove(True):",v)
"""
