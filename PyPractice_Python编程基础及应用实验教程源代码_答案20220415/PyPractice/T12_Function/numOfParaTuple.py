def clac(*num):
    s=0
    for i in num:
        s=s+i
    return s
	
result1 = clac(1,2,3,4)
result2 = clac(12,-1,100,30,49,50)
print(result1,result2)
