def calc(*num):
    s=0
    for i in num:
        s=s+i
    return s

result1=calc(1,2,3,4)
result2=calc(12,-1,100,30,49,50)
print(result1,result2)