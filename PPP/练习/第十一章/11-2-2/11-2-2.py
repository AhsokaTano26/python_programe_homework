c = 0
e = []
h = []
with open("text.txt", "r") as f:
    for x in f.readlines():
        g = x.split(" ")
        for i in g:
            e.append(i)
        c += 1
with open("text.txt", "r") as f:
    while True:
        d = f.read(1)
        if d != " ":
            h.append(d)
        if not d:
            break
b = len(e)
h.remove("\n")
h.remove("")
a = len(h)
print(h)
print(a)
print(b)
print(c)