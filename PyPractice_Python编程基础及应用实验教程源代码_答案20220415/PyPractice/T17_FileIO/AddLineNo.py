with open("AddLineNo.py","rt") as f:
    lines = f.readlines()

maxLength = len(max(lines,key=len))

newLines = [line.rstrip().ljust(maxLength) + \
    "#" +str(r+1) + "\n" for r,line in enumerate(lines)]

with open("AddLineNo2.py","wt") as f:
    f.writelines(newLines)
