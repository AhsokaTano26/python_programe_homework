x,y=eval(input())
assert x!=0 and y!=0
if x>0:
    if y>0:
        print("第1象限")
    else:
        print("第4象限")
else:
    if y>0:
        print("第2象限")
    else:
        print("第3象限")