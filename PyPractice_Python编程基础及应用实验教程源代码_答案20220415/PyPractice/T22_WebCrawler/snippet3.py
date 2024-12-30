import re
print(re.findall('w{3}\.([a-zA-Z]+\.)+com', 'www.baidu.com'))
print(re.findall('w{3}\.([a-zA-Z]+\.)+com', 'www.baidu.com \
    www.baidu.edu.com'))
