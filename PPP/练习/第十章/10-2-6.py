a = input()
b = input()
if len(a) == len(b):
    for x in a:
        if a.count(x) != b.count(x):
            print('False')
            break
    else:
        print('True')

else:
    print('False')