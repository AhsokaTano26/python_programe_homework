a = input()
xi = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
n = [1,0,'X',9,8,7,6,5,4,3,2]
c = 0
if len(a)==18:
    for x in range(len(a)-1):
        b = int(a[x])*xi[x]
        c += b
    d = c%11
    m = n[d]
    if a[-1]==str(m):
        print('Correct')
    else:
        print('Wrong')
else:
    print('Error')