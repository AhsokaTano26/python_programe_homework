from math import ceil

def findFalseCoin(coins,idxStart,iLength):
    if iLength == 1:
        return idxStart

    n = ceil(iLength/3)
    wPart1 = sum(coins[idxStart:idxStart+n])
    wPart2 = sum(coins[idxStart+n:idxStart+2*n])
    wPart3 = sum(coins[idxStart+2*n:idxStart+iLength])
    if wPart1 < wPart2:
        return findFalseCoin(coins,idxStart,n)
    elif wPart1 > wPart2:
        return findFalseCoin(coins,idxStart+n,n)
    else:
        return findFalseCoin(coins,idxStart+2*n,iLength-2*n)
    
if __name__ == '__main__':
    coins  = [100,100,100,100,100,100,100,100,100,100,100]

    for i in range(len(coins)):
        coinsCopy = coins[:]
        coinsCopy[i] = 99
        r = findFalseCoin(coinsCopy, 0, len(coinsCopy))
        print(f'False coin idx:{r}, weight:{coinsCopy[r]}')
