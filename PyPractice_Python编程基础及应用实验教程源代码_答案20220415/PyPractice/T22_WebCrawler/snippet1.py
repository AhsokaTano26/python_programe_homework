import re 
#在起始位置匹配 
print(re.match('www','www.cqu.edu.cn').span())
#不在起始位置匹配
print(re.match('cn','www.cqu.edu.cn').span())  #匹配失败，抛出异常。
