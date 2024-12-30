f = open("abc.txt")
print("abc.txt: ",f.read())

f = open("d:\\pypractice\\t17_fileio\\abc.txt")
print("d:\\pypractice\\t17_fileio\\abc.txt: ",f.read())

f = open("../t21_cellcounter/cellcounter.py")
print("first line of cellcounter.py(1): ",f.readline())

f = open("d:/PyPractice/T21_CellCounter/CellCounter.py")
print("first line of cellcounter.py(2): ",f.readline())
