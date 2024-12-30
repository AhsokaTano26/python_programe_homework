n = eval(input())
#生成每行均为最后一行的一个二维列表
lst = [[chr(ord("A") + a) for a in range(n)] for b in range(n)]
for i in range(n):
        for j in range(i+1,n):
                lst[i][j] = chr(ord("A")+i)
        #打印输出第i行
        print("".join(lst[i]))