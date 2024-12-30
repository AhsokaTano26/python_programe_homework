name = input()
grade = eval(input())
name = name.split(',')
a = len(grade)
b = [[] for i in range(a)]
for i in range(0,a,1):
    b[i].append(name[i])
    b[i].append(grade[i])
print(b)
