import re 
#在起始位置匹配 
print(re.search('www','www.163.com').span())
#不在起始位置匹配
print(re.search('com','www.163.com').span())
