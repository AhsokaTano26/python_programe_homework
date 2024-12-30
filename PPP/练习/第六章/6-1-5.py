nums = eval(input())
sum = eval(input())
for x in range(len(nums)):
        n = sum-nums[x]
        if n in nums:
            if n != nums[x]:
                print(True)
                break
            else:
                if nums.count(n) >= 2:
                    print(True)
                    break
else:
    print(False)