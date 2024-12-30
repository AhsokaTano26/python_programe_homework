import random, math

def gambleOnce():
    return random.random() > 0.5

def gambleDay(money):
    if money < 1: 
        return money 

    wager = 1 
    money -= wager
    
    while not gambleOnce(): 
        wager *= 2
        money  -= wager
        if money <= 0: 
            return money 

    money = money + 2 * wager
    return money

if __name__ == '__main__':
    iWinner, iLoser = 0,0
    for x in range(100):
        moneyHold = 1024
        moneyHolds = []

        dayNumber =  3650*2
        for x in range(dayNumber): 
            moneyHold = gambleDay(moneyHold)
            moneyHolds.append(moneyHold)
        
        if moneyHold > 0:
            iWinner += 1
        else:
            iLoser += 1
    
    print(f"Winner: {iWinner}, Loser: {iLoser}")



    