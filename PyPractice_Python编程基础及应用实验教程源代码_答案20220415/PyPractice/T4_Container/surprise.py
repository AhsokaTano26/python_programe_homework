v = [1,True,2,True,0,False]
print(v)
print("count/1:", v.count(1), ",count/True:", v.count(True))
print("count/0:", v.count(0), ",count/False:", v.count(False))
print("idx/True:",v.index(True), ",idx/False",v.index(False))
v.remove(True)
print("after v.remove(True):",v)
print("1==True:",1==True,",0==False:",0==False)
