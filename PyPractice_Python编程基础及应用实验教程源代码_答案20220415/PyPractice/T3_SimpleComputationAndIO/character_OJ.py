Q = input()
N = int(input())
n = ord(Q) - ord('A') + 1
print(f"{Q}是字母表中第{n}个字母.")
c = chr(ord('A') + N - 1)
print(f"字母表中第{N}个字母是{c}.")
