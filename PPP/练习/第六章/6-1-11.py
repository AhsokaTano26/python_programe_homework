def main():
    a = int(input())
    calculate_sum(a)
def calculate_sum(a):
    b = 0
    c = a
    if a < 10:
        for i in range(a):
            b = b + a
            a = c + a * 10
    else:
        for i in range(a):
            b = b + a
            a = c + a * 100
    print(b)
main()
