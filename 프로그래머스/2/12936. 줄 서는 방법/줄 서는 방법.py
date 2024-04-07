import math


def solution(n, k):
    mul = 1
    i = 1
    ls = []
    while mul <= k:
        mul *= i + 1
        i += 1
    mul //= i

    use = [False] * (n + 1)
    if i < n:
        ls = [i for i in range(1,  n + 1)][: -i]
    for j in ls:
        use[j] = True

    while True:
        t = [i for i in range(1, n + 1) if not use[i]][math.ceil(k / mul) - 1]
        ls.append(t)
        use[t] = True

        if len(ls) == n:
            break

        k = k % mul
        i -= 1
        mul //= i

    return ls
