def maxsum(num):
    num.sort()
    b = len(num)
    c = num[0]
    if b >= 0:
        for i in range(2,b,2):
            c = c + num[i]
    return c
nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

