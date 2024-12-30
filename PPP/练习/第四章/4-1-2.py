def calDegrees(nums):
    a = max(nums,key=nums.count)
    b = 0
    for i in nums:
        if i == a:
            b = b + 1
    return b
nums = eval(input())
d = calDegrees(nums)  #调用自定义函数
print(d)
