def key(sName="Peter",**course):
     sum=0
     for i,j in course.items():
          print(i,":",j)
     for i in course.values():
          sum=sum+i
     avg=sum/len(course)
     print("{}'s average score is:{:.2f}".format(sName,avg))

key(math=90,english=88,python=95,sports=76)
          

