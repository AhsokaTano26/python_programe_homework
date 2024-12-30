def explore(d, m, n, i, j):                   #对图像宽度优先遍历
    q = [(i, j)]
    while q:
        x, y = q.pop(0)
        if d[x][y] < 0:
            continue
        d[x][y] = 0 - d[x][y]
        if x > 0 and d[x - 1][y] > 0:
            q.append((x - 1, y))
        if x < (m - 1) and d[x + 1][y] > 0:
            q.append((x + 1, y))
        if y > 0 and d[x][y - 1] > 0:
            q.append((x, y - 1))
        if y < (n - 1) and d[x][y + 1] > 0:
            q.append((x, y + 1))

d = []                                        #从文件中读取二值化数据并打印
with open('cellpicture.txt') as f:
    m,n = map(int,f.readline().split())       #读取矩阵的行数和列数
    for x in range(m):                        #读取二值化数据的每一行，并将其作为一个列表添加至空列表d
        r = list(map(int, f.readline()[:n]))
        d.append(r)

for x in d:
    print(x)                                  #打印读取的二值化数据矩阵

iCellCount = 0                                #计算细胞个数
for i in range(m):                            #遍历矩阵的行
    for j in range(n):                        #遍历矩阵的列
        if d[i][j] <= 0:
            continue
        iCellCount += 1                       #细胞计数器计数加一
        explore(d,m,n,i,j)                    #调用图的宽度优先遍历

print(iCellCount)                             #打印细胞个数
print(m)
print(n)
