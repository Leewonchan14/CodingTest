def main(n, k):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[1] = [1] * (n + 1)

    for kk in range(1, k + 1):
        for nn in range(n + 1):
            sumv = dp[kk][nn]
            for j in range(nn + 1):
                sumv = (sumv + dp[kk - 1][j]) % 10**9
            dp[kk][nn] = sumv

    return dp[k][n]


a, b = [int(i) for i in input().split()]
print(main(a, b))
