def in_strict(x, v):
    for e in v:
        if type(e) == type(x) and e == x:
            return True
    return False

v = list(eval(input("input:")))
print("before:",v)
v = [x for i, x in enumerate(v) if not in_strict(x, v[i + 1:])]
print("after:",v)