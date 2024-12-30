def find_fff(lst):
    lst1 = []
    for i in lst:
        if lst.count(i)<2 and i not in lst1:
            lst1.append(i)
    return lst1

lst = eval(input())
a = list(lst)
a.sort()
b = find_fff(a)
if len(b) < 1:
    print("False")
else:
    c = ','.join(str(i) for i in b)
    print(c)
