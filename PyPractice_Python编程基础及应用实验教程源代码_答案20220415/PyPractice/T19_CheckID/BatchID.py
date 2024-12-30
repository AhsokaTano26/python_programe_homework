weights = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
m = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

def checkID(sID):
    if len(sID)!=18:
        return False
    sum = 0 
    for i in range(17):
        c = sID[i]
        if ord(c)<ord('0') or ord(c)>ord('9'):
            return False 
        sum += weights[i] * int(c)
    z = sum % 11
    if m[z] != sID[17]:
        return False 
    return True

progressBefore = 0
def printProgressBar(percent, prefix = ''):
    global progressBefore
    if percent - progressBefore < 0.001 and percent < 1.0:	#只有当进度达到千分之一才刷新，避免频繁刷新进度条
        return
    progressBefore = percent
    percentStr = ("{0:.1f}").format(percent*100) #格式化字符串，参见字符串进阶一章相关内容
    filledLength = int(30 * percent)
    bar = '█' * filledLength + '-' * (30 - filledLength)
    print('\r%s |%s| %s%% '%(prefix, bar, percentStr),end="")


f = open("ids.txt","rt")
fError = open("error.txt","wt")
lines = f.readlines()
linesCount = len(lines)
linesProcessed = 0
for sID in lines:
    if not checkID(sID[:-1]):
        fError.write(sID)
    linesProcessed += 1
    printProgressBar(linesProcessed/linesCount,"身份证查验中")
fError.close()
f.close()