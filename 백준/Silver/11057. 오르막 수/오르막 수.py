def main(n):
    dp = [([1] * 10) for i in range(n + 1)]

    for k in range(2, n + 1):
        for i in range(1, 10):
            dp[k][i] = (dp[k - 1][i] + dp[k][i - 1]) % 10007

    return sum(dp[n]) % 10007


print(main(int(input())))
