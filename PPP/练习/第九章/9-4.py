class  Stock:
    'Stock Information Class'
    def __init__(self,sCode,sName,priceYesterday,priceToday):
        self.Code=sCode
        self.Name=sName
        self.priceYesterday=priceYesterday
        self.priceToday=priceToday
    def getCode(self):
        return self.Code
    def getName(self):
        return self.Name
    def getPriceYesterday(self):
        return self.priceYesterday
    def getPriceToday(self):
        return self.priceToday
    def setPriceYesterday(self,price):
        self.priceYesterday=price
    def getChangePercent(self):
        return (self.priceToday-self.priceYesterday)/self.priceYesterday
sCode  =  input()  #Stock  Code
sName  =  input()  #Stock  Name
priceYesterday  =  float(input())    #Price/Yesterday
priceToday  =  float(input())    #Price  Today
s  =  Stock(sCode,sName,priceYesterday,priceToday)
print("Code:",s.getCode())
print("Name:",s.getName())
print("Price/Yesterday:%.2f\nPrice  Today:%.2f"  %  (s.getPriceYesterday(),s.getPriceToday()))
s.setPriceYesterday(50.25)
print("Edit  Price/Yesterday  To:%.2f"  %50.25)
print("Price  Change  Percentage:%.2f%%"  %  (s.getChangePercent()*100))
print(Stock.__doc__)