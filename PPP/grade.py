name1,s11,s12 = map(str,input().split())
name2,s21,s22 = map(str,input().split())
name3,s31,s32 = map(str,input().split())
name4,s41,s42 = map(str,input().split())
name5,s51,s52 = map(str,input().split())
s11,s12,s21,s22,s31,s32,s41,s42,s51,s52 = int(s11),int(s12),int(s21),int(s22),int(s31),int(s32),int(s41),int(s42),\
    int(s51),int(s52)
def score(score1,credit):
    sc = 4.0*(90 if score1>90 else score1)/90
    score = sc*credit
    return score
GPA = (score(s11,s12)+score(s21,s22)+score(s31,s32)+score(s41,s42)+score(s51,s52))/(s12+s22+s32+s42+s52)
print("GPA:%.2f" % GPA)

