d = []
with open('cellpicture.txt') as f:
    m,n = map(int,f.readline().split())
    for x in range(m):
        r = list(map(int, f.readline()[:n]))
        d.append(r)

for x in d:
    print(x)

def explorePixel(d,m,n,i,j):
        q = [(i,j)]
        while q:
            x,y = q.pop(0)
            if d[x][y] < 0:
                continue 
            d[x][y] = 0-d[x][y]
            if x>0 and d[x-1][y]>0:
                q.append((x-1,y))
            if x<(m-1) and d[x+1][y]>0:
                q.append((x+1,y))
            if y>0 and d[x][y-1]>0:
                q.append((x,y-1))
            if y<(n-1) and d[x][y+1]>0:
                q.append((x,y+1))

iCellCount = 0
for i in range(m):
    for j in range(n):
        if d[i][j] <= 0:
            continue
        iCellCount += 1
        explorePixel(d,m,n,i,j)

print(iCellCount)
