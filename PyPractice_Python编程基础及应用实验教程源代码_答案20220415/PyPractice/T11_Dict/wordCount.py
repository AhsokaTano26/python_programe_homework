txtWord=open("word.txt","r").read()
txtWord=txtWord.lower()
counts={}
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txtWord = txtWord.replace(ch, " ")   #将文本中特殊字符替换为空格
words=txtWord.split()
for word in words:
    if word in counts:
        counts[word]=counts[word]+1
    else:   
        counts[word]=1 #统计功能也可以使用字典的get方法实现
items=[[x,y] for (y,x) in list(counts.items())]
items.sort(reverse=True)
print(items)

