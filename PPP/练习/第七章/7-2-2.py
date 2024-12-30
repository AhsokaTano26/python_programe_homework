dic = {}
lst = []
count = 0
while True:
    a = input()
    if a == "q":
        break
    lst.append(a)
for x in lst:
    dic[x] = lst.count(x)
d = max(dic.values())
for k in dic:
    if dic[k] == d:
        print(k,d)