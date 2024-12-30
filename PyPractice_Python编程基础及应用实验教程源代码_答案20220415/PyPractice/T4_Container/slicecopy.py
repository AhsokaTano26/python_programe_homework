a = [1,2,3,4,5,6,7]
b = a
c = a[:]
a[3:5] = 99,100
print("a=",a,"id(a)=",id(a))
print("b=",b,"id(b)=",id(b))
print("c=",c,"id(c)=",id(c))
