#1. 题库：对文件内每个字符进行大小写转换处理并输出！
#【问题描述】对文件内每个字符进行大小写转换处理！

#【输入形式】文本文件
#【输出形式】输出转换后的内容
#【样例输入】data.txt
#【样例输出】

#SNOSNAMESAGE

#1ZS18

#2LS20

#3WW21

#【样例说明】输出转换后的内容

#【评分标准】 通过所有的测试用例
with open("data.txt") as f:
    for x in f.readlines():
        print(x.upper())