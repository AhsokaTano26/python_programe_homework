a = str(input())
for x in a:
    if a.count(x)==1:
        print(x)
        break
else:
    print('None')