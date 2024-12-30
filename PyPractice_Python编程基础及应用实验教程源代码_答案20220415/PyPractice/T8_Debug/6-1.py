def main():  #最大子段和
    s = [12,-4,32,-36,12,6,-6]
    s_max, s_sum = 0, 0
    for i in range(len(s)):
        s_sum += s[i]
        if s_sum >= s_max:
            s_max = s_sum
        elif s_sum < 0:
            s_sum = 0
    print(s_max)

main()