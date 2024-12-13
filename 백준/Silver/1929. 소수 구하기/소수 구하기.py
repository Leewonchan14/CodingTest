def che():
    maxv = 10 ** 6
    dp = [True] * (maxv + 1)
    dp[0] = False
    dp[1] = False
    for i in range(2, maxv + 1):
        if dp[i]:
            for j in range(i + i, maxv + 1, i):
                dp[j] = False
    return dp

dp = che()
a, b = map(int, input().split())
for i in range(a, b + 1):
    if dp[i]:
        print(i)
