def recur(n, k, c):
    rt = 0

    if k == 1:
        rt = n

    elif k % 2 == 0:
        nn = recur(n, k // 2, c)
        rt = nn**2

    else:
        nn = recur(n, (k - 1) // 2, c)
        rt = nn**2 * n

    return rt % c


a, b, c = [int(i) for i in input().split()]
a %= c

print(recur(a, b, c))
