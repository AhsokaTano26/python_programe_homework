def costCompute(iStart, iEnd):
    iConsume = iEnd - iStart
    return iConsume * 0.85


fElec1, fElec2 = eval(input())
fee = costCompute(fElec1, fElec2)
print("%.2f" % fee)