v = eval(input())
limit = eval(input())
r = (v-limit)/limit
if v <= limit:
    print("未超速")
elif r <= 0.1:
    print("超速警告")
elif r <= 0.2:
    print("罚款100元")
elif r <= 0.5:
    print("罚款500元")
elif r <= 1.0:
    print("罚款1000元")
else:
    print("罚款2000元")