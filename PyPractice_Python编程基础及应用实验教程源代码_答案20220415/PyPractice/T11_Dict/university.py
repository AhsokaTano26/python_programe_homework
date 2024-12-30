infile=open("university.txt","r").readlines()
universityDict={}
for line in infile:
     lst=line.split()
     universityDict[lst[0]]=int(lst[1])
items=list(universityDict.items())
items.sort(key=lambda x:x[1],reverse=True)
print(items[0])
sum=0
for i in universityDict.values():
     sum=sum+int(i)
print(sum)


