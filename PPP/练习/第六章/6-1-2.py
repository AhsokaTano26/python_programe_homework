def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a = 1
    e = 1
    for x in range(1,int(num)+1):
        a = a*(1/x)
        e = e + a
    print("%.6f" % e)
main()