def isPass(score,n=60):
    if score>=n:
        return "passed"
    else:
        return "failed"

stuA=80
print(isPass(stuA))
stuB=120
print(isPass(stuB,90))
