v = input().split()
score1 = int(v[1])
credit1 = int(v[2])

v = input().split()
score2 = int(v[1])
credit2 = int(v[2])

v = input().split()
score3 = int(v[1])
credit3 = int(v[2])

v = input().split()
score4 = int(v[1])
credit4 = int(v[2])

v = input().split()
score5 = int(v[1])
credit5 = int(v[2])

gpa = 0
score = score1
gpa += credit1*4.0*(90 if score > 90 else score)/90
score = score2
gpa += credit2*4.0*(90 if score > 90 else score)/90
score = score3
gpa += credit3*4.0*(90 if score > 90 else score)/90
score = score4
gpa += credit4*4.0*(90 if score > 90 else score)/90
score = score5
gpa += credit5*4.0*(90 if score > 90 else score)/90
gpa /= (credit1+credit2+credit3+credit4+credit5)
print(f"GPA:{gpa:.2f}")
