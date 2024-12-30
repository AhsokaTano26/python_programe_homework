v = input("")
a,b,c,d = map(int,v.split())
delta = (c*60 + d) - (a*60 + b)
m = delta % 60
h = (delta - m)//60
print(f"{h}:{m}")


