def  work(a)  :
    ans = {0:1}
    b = 1
    for x in range(1,a+1) :
        b = b * x
        ans[x] = b
    return ans
a = int(input())
ans = work(a)
print(ans)