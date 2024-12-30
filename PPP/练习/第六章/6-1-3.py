def  leapyear(x):
    return x % 400 == 0 or (x % 100 != 0 and x % 4 == 0)
year = int(input())
if leapyear(year):
    print("In %d February has 29 days." % year)
else:
    print("In %d February has 28 days." % year)