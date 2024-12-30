def add(dic):
     for i in dic.keys():
          dic[i]=dic[i]+10
     return dic

score={"zhangsan":80,"李四":50,"wangwu":40}
scoreChange=add(score)
print(score)
print(scoreChange)
          
