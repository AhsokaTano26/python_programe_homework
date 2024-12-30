def num(a):
    color = ["red", "blue", "yellow"]
    for i in range(3):
        if a == color[i]:
            return i+1
c1 = input()
c2 = input()
color = ["red","blue","yellow"]
if c1 in color and c2 in color:
    if c1 != c2:
        cn1 = num(c1)
        cn2 = num(c2)
        if cn1 == 1:
            if cn2 == 2:
                sc = "purple"
            else:
                sc = "orange"
        elif cn1 == 2:
            if cn2 == 1:
                sc = "purple"
            else:
                sc = "green"
        else:
            if cn2 == 1:
                sc = "orange"
            else:
                sc = "green"
    else:
        sc = "error"
else:
    sc = "error"
print(sc)