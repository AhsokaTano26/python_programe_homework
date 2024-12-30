def add_id(data2):
    for x in range(len(data2)):
        data2[x] = str(data2[x])
        data2[x] = "20" + data2[x]
    return data2


data1 = input().split()
result = add_id(data1)
for x in result:
    print(x, end=" ")