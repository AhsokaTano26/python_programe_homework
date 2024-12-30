def main():
    stra = input()
    lista = list(stra)
    print(''.join(replace_stars(lista)))


def replace_stars(str_list):  # 将所有*号移动到数组的左侧
    j = len(str_list) - 1
    for i in range(j, -1, -1):
        if str_list[i] != '*':
            str_list[i], str_list[j] = str_list[j], str_list[i]
            j -= 1
    return str_list


main()