#【问题描述】逐行读取data.txt文件信息并显示。
#【输入形式】文件输入
#【输出形式】逐行输出文件内的信息
#【样例输入】data.txt
#【样例输出】

#sno sname sage

#1     zs        18
#【样例说明】输出文件中的每行信息
#【评分标准】通过所有测试用例

with open('data.txt', 'r') as f:
    for  line  in  f.readlines():
            line  =  line.strip('\n')
            print(line)
f.close()