N = int(input("请输入N:"))

iCount = 0
for men in range(N+1):
    for women in range(N+1):
        for children in range(N+1):
            if men + women + children == N and men*3 + women*2 + children//2 == N and children%2==0:
                print(f"找到解：men={men},women={women},children={children}")
                iCount += 1
                
print("解的数量:",iCount)
