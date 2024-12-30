import random 
weights = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
m = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

def generateID():
    sArea = str(random.randint(100000,999999))
    sYear = str(random.randint(1900,2021))
    sMonth = ['01','02','03','04','05','06','07','08','09','10','11','12'][random.randint(0,11)]
    sDay = str(random.randint(1,28))
    sDay = "0"*(2-len(sDay)) + sDay
    sOrder = str(random.randint(0,999))
    sOrder = "0"*(3-len(sOrder)) + sOrder 
    sID = sArea + sYear + sMonth + sDay + sOrder
    sum = 0 
    for i in range(17):
        sum += int(sID[i])*weights[i]
    z = sum % 11
    sID = sID + m[z]
    return sID

f = open("ids.txt","wt")
for i in range(100000):
    sID = generateID()
    f.write(sID + "\n");
f.close()

print("100000 lines written to file ids.txt")