weights = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
m = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

def checkID(sID):
    if len(sID)!=18:
        return False
    sum = 0 
    for i in range(17):
        c = sID[i]
        if ord(c)<ord('0') or ord(c)>ord('9'):
            return False 
        sum += weights[i] * int(c)
    z = sum % 11
    if m[z] != sID[17]:
        return False 
    return True

print("320124198808240056:", checkID("320124198808240056"))
print("360402197901160035:", checkID("360402197901160035"))
print("36040219160035:", checkID("36040219160035"))
print(":", checkID(""))
print("3604021979011600351234:", checkID("3604021979011600351234"))
print("360C0219160035:", checkID("360C0219160035"))
    