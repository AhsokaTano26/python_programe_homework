N = int(input("请输入N:"))

iCount = 0
for men in range(N//3+1):
    for women in range(N//2+1):
        children = N - men - women 
        if men*3 + women*2 + children//2 == N and children%2==0:
            print(f"找到解：men={men},women={women},children={children}")
            iCount += 1
                
print("解的数量:",iCount)
