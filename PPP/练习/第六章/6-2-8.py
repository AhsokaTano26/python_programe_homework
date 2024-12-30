a = list(input())
alphaNum = 0
numberNum = 0
spaceNum = 0
elseNum = 0
for i in a:
    if i.isalpha():
        alphaNum += 1
    elif i.isnumeric():
        numberNum += 1
    elif i.isspace():
        spaceNum += 1
    else:
        elseNum += 1
print(alphaNum,spaceNum,numberNum,elseNum)
