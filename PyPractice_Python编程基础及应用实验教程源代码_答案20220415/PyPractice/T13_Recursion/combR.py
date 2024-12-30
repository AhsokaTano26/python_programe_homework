def combinatorial(n, k):
    if n < k: #基例
        return 0
    if n == k or k == 0 : #基例
        return 1
    else: #链条
        return combinatorial(n-1, k) + combinatorial(n-1, k-1)

print(combinatorial(5,3))
