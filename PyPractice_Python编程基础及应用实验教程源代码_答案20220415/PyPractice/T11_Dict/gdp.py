GDP={"CN":15.63,"US":20.9,"DE":3.78,"JP":5.13}
print(len(GDP))
GDP["UK"] = 2.59
print(GDP)
GDP["JP"] = 5.23
del GDP["DE"]
GDP1= GDP
print(GDP==GDP1)
print(GDP is GDP1)
GDP1 = GDP.copy()
print(GDP1)
print(GDP==GDP1)
print(GDP is GDP1)
print("CN" in GDP)
print(20.9 in GDP)
print(GDP["CN"])
print(GDP.get("CN",999))
# print(GDP["FR"])
print(GDP.get("FR",0))
GDP2={"IT":1.84,"ES":1.24,"DE":2.78,"JP":5.23}
GDP.update(GDP2)
print(GDP)
GDP.clear()
print(GDP)


