str1 = input()
a = 0
b = '~!@#$%^&*()_=-/,.?<>;:[]{}|\\'
if any(chr.isdigit() for chr in str1)==True:
    a += 1
if any(chr.islower() for chr in str1)==True:
    a += 1
if any(chr.isupper() for chr in str1)==True:
    a += 1
if len(str1)>=8:
    a += 1
for x in str1:
    if x in b:
        a += 1
        break
print(a)