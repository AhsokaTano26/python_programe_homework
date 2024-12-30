infile=open("university1.txt","r",encoding="utf-8").readlines()
universityDict={}
lst=[]
for line in infile:
     temp=[]
     lst=line.split()     
     for i in range(1,len(lst)):
         temp.append(int(lst[i]))
     universityDict[lst[0]]=temp
province=input("请输入省名：")
strTemp=""
if province in universityDict.keys():
     strTemp="{}大学数量：{}，双一流高校建设数量：{}，一流大学建设高校数量：\
     {}，一流学科建设高校数量：{}。".format(province,universityDict[province][0],\
     universityDict[province][1],universityDict[province][2],universityDict[province][3])
     print(strTemp)
items=list(universityDict.items())
items.sort(key=lambda x:(x[1][1],x[1][2]),reverse=True)
print(items)
sum1=0
sum2=0
for i in universityDict.values():
     sum1=sum1+i[1]
     sum2=sum2+i[2]
print("中国双一流建设高校的数量:",sum1,"一流大学建设高校数量:",sum2)     




