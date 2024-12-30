a = input()
print(a)
for x in a:
    if x.isalpha():
        if x.islower():
            x=chr(25-ord(x)+ord('a')*2)
            print(x,end='')
        else:
            x=chr(25-ord(x)+ord('A')*2)
            print(x,end='')
    else:
        print(x,end='')