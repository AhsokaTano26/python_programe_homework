def aaa(lll):
    if len(lll) == 0:
        a = "False"
    else:
        a = lll[0]
    return a
def search(nums):
    lll = []
    numbs1 = len(nums)
    numbs2 = numbs1//2
    for i in nums:
        if nums.count(i) > numbs2:
            lll.append(i)
    return aaa(lll)
nums = eval(input())
y = search(nums)
print(y)
