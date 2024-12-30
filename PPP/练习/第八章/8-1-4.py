def count_foreign(ids):
    m = 0
    for x in ids:
        x = str(x)
        if x[0] == "L" and len(x) == 9:
            m += 1
    return int(m)


origin = input().split()
print(count_foreign(origin))