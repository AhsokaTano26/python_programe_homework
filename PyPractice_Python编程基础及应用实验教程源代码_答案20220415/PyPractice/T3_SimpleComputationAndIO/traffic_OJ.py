m = int(input())
n = int(input())
y = (n*6-m*8)/(n-m)
x = m*8 - m*y
z = x / (10-y)
print(f"原有排队游客份数:{x:.1f}, 每分钟新到游客份数:{y:.1f}, 10口同开需{z:.1f}分钟清零待检票游客.")
