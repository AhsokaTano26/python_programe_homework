gpa = 0
score = 78
gpa += 3*4.0*(90 if score > 90 else score)/90
score = 91
gpa += 5*4.0*(90 if score > 90 else score)/90
score = 65
gpa += 4*4.0*(90 if score > 90 else score)/90
score = 95
gpa += 3*4.0*(90 if score > 90 else score)/90
score = 60
gpa += 2*4.0*(90 if score > 90 else score)/90
gpa /= (3+5+4+3+2)
print("GPA:",gpa)
