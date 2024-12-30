leapYears = [x for x in range(2000,3001) if \
    (x % 4 == 0 and x % 100 !=0) or (x % 400 == 0) ]
print("Leap years(2000~3000):", leapYears[::10])