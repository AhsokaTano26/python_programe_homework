n = eval(input(""))
txtWord = ""
for i in range(n):
    txtWord = txtWord + " " + input()

counts={}
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~0123456789\'':
        txtWord = txtWord.replace(ch, " ")   #将文本中特殊字符替换为空格

txtWord = txtWord.lower()
words=txtWord.split()

for word in words:
    if word in counts:
        counts[word]=counts[word]+1
    else:   
        counts[word]=1 #统计功能也可以使用字典的get方法实现

items=[[x,y] for (x,y) in list(counts.items())]
items.sort()
for k,v in items:   #按数量、单词递增序排序
    print(k,v)

