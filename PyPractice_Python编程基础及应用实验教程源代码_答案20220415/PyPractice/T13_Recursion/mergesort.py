def merge_sort(lst):
    if len(lst) <= 1: 
        return lst
    
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left,right)

def merge(A,B):
    if len(A) == 0:   
        return B
    if len(B) == 0:   
        return A
    if A[0] > B[0]:     
        return [B[0]] + merge(A,B[1:])
    else:
        return [A[0]] + merge(A[1:],B)


lst = [-9,10,1,5,3,7,8,10]
print(merge_sort(lst))