y = eval(input())

if y%400==0:
    print("闰年")
elif y%100==0:
    print("平年")
elif y%4==0:
    print("闰年")
else:
    print("平年")
