class Book:
    def __init__(self, name, no, price):
        self.sName = name
        self.sNo = no
        self.fPrice = price

    def __del__(self):
        print('Book destroyed-%s,%s,%.2f' % (self.sName, self.sNo, self.fPrice))


sName = input()
sNo = input()
fPrice = float(input())
b = Book(sName, sNo, fPrice)