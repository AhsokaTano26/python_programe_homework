total = 0
count = 0
while True:
    a = input()
    if a == '#':
        break
    total = total + int(a)
    count = count + 1
print(count,total)