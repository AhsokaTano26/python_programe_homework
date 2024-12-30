def deposit(n):
    s=0
    for i in range(0,n):
        s=s+pow(2,i)
    return s/100

def withdraw(n,amount):
    s=0
    for i in range(0,n):
        s=s+amount
    return s

days,amount=eval(input("Please enter days and amount:"))
diff=deposit(days)-withdraw(days,amount)
if diff>0:
    print("The loss is {:.4f}".format(diff))
else:
    print("The profit is {:.4f}".format(diff))
