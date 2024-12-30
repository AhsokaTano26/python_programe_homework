def    myFun(a,b):
    if int(a)<=0 or int(b)<=0:
        return 'error'
    else:
        a,b = str(a),str(b)
        total = 0
        if len(a)>len(b):
            b = '0'*(len(a)-len(b)) + b
            for x in range(len(a)):
                every = int(a[x])*int(b[x])
                total += every
            return total
        elif len(a)<len(b):
            a = '0'*(len(b)-len(a)) + a
            for x in range(len(b)):
                every = int(a[x])*int(b[x])
                total += every
            return total
        else:
            for x in range(len(b)):
                every = int(a[x])*int(b[x])
                total += every
            return total

num=input().split()
a=num[0]
b=num[1]
if  a.isdigit()  and  b.isdigit():  #判断a,b是否都是数字
    print(myFun(a,b))    #调用自定义函数
else:
    print("error")