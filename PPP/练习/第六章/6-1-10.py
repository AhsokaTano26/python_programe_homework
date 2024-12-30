def main():
    total_count = int(input())
    calculate_days(total_count)
def calculate_days(a):
    b = 0
    while a // 1 > 0:
        a = a - ((a//2)+2)
        b = b + 1
    print(b)
main()