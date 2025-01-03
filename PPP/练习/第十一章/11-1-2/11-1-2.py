#【问题描述】输入学生个人信息，并写入到文件data.txt中。

#【输入形式】输入学生个人信息，包括学号，姓名及年龄，用逗号隔开

#【输出形式】输出每个学生的学号，姓名及年龄
#【样例输入】

#1,zs,18

#2,ls,21

#End
#【样例输出】

#sno sname sage

#1   zs    18

#2   ls    21

#【样例说明】输入的学生信息用“End”结束
#【评分标准】通过所有测试用例

f = open("data.txt","r+")
f.write("sno\tsname\tsage\n")
stext = input() or "End"
while stext != "End":
    stu = stext.split(",")
    for i in stu:
        f.write(i + "\t")
    stext = input() or "End"
f.seek(0)
print(f.read())
f.close()