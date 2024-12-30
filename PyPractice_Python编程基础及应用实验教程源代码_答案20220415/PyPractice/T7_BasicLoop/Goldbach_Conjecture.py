import math
def isPrime(num):
   if num < 0 or num in (0,1):
      return  False  
   for i in range(2,int(math.sqrt(num))+1):
      if num % i == 0:
         return  False
   return True

n = int(input())
for i in range(2,n):
    j = n - i
    if isPrime(i) and isPrime(j):
        print("%d = %d + %d" % (n,i,j))
        break