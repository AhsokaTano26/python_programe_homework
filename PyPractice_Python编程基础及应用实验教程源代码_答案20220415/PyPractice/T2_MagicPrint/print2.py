from prettytable import PrettyTable

t = PrettyTable(["序号","课程","成绩","学分"])
t.add_row([1,"程序设计基础",98,2])
t.add_row([2,"大学物理(1)",89,3])
t.add_row([3,"高等数学(1)",75,3])
t.add_row([4,"大学英语(1)",100,3])

print(t)