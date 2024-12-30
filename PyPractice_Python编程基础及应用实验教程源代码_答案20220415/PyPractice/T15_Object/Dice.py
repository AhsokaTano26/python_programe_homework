import random
class Dice: 
    def __init__(self,sides=6):
        self.iSides = sides
        self.results = []

    def rollDice(self):
        r = random.randint(1,self.iSides)
        self.results.append(r)
        return r

    def sideCount(self,side):
        return self.results.count(side)

    def rollCount(self):
        return len(self.results)

d = Dice()
print("-----Roll dice for 100 times-----")
for x in range(100):
    r = d.rollDice()
    if x < 10:
        print(r,end=",") 
print("...")

print("-----Statistics of rolling the dice-----")
for i in range(1,d.iSides+1):
    sideCount = d.sideCount(i)
    rollCount = d.rollCount()
    print(f"Side {i}: {sideCount}/{rollCount} = "\
        f"{sideCount*100/rollCount:.1f}%")
    