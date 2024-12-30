def getdata( ):
    """从文件读取应聘者信息"""
    listtemp=[]

    with open("data.txt","r") as f:
        while True:
            strTemp = f.readline()
            if not strTemp:
                break
            listtemp.append(strTemp.split())

    return listtemp

def classify(listT):
    """把满足要求的应聘者分成4类"""
    a, b, c, d = [],[],[],[]
    for m in listT:
        pScore=int(m[1])
        tScore=int(m[2])
        if pScore>=60 and tScore>=60:
            if pScore>=80 and tScore>=80:
                a.append(m)
            elif pScore>=80:
                b.append(m)
            elif pScore>=tScore:
                c.append(m)
            else:
                d.append(m)
    return a,b,c,d

def admissionSort(a,b,c,d):
    """分别对四类人员按总分，实践分降序，报名号升序排序"""
    listA = []#按录取规则顺序存放招聘人员信息
    for i in (a,b,c,d):
        i.sort(key=lambda x : (-(int(x[1])+int(x[2])),-int(x[1]),int(x[0])))
        listA =listA+i
    return listA 

def myPrintL(listA):
    """输出录取人数和按录取顺序排列的应聘者名单"""
    print("上线人数",len(listA))
    for j in listA:
        print(" ".join(j))

def main():
    listA = getdata()#获取原始数据
    a, b, c, d = classify(listA)
    admissionList=admissionSort( a, b, c, d)#生成录取顺序名单
    myPrintL(admissionList)

main()
