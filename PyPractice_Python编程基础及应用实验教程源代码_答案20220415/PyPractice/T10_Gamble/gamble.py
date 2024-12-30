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
    moneyHold = 1024
    moneyHolds = []

    dayNumber =  365
    for x in range(dayNumber): 
        moneyHold = gambleDay(moneyHold)
        moneyHolds.append(moneyHold)

    from matplotlib import pyplot as plt 
    plt.scatter(list(range(1,dayNumber+1)), moneyHolds, s = 1)                                                                            
    plt.title(f'Every day\'s money during {dayNumber} days') 
    plt.show() 
    