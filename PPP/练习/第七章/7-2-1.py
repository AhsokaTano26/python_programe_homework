GDP = {}
country = []
gdp = []
total = 0
while True:
    a = input()
    if a == "ok":
        break
    b,c = a.split()
    country.append(b)
    gdp.append(int(c))
    GDP[b] = int(c)
gdp.sort()
country.sort()
if "India" in country:
    d = "yes"
else:
    d = "no"
for i in gdp:
    total = total + i
print(country)
print(gdp)
print(d)
print(total)
