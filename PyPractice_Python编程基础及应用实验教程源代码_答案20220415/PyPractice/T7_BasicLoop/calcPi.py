fError = 1e-8
iDenominator = 1
bAdd = True
fPi = 0.0
fItem = 1.0 / iDenominator
while fItem >= fError:
    fPi = fPi + fItem if bAdd else fPi - fItem
    iDenominator += 2
    fItem = 1.0/iDenominator
    bAdd = not bAdd 

print("pi = %.15f" % (fPi * 4.0))