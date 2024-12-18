dp = [[], [0, *([1] * 9)]]

n = int(input())

for i in range(len(dp), n + 1):
    dp.append([0] * 10)
    for j in range(10):
        a = dp[-2][j - 1] if j - 1 >= 0 else 0
        b = dp[-2][j + 1] if j + 1 <= 9 else 0
        dp[-1][j] = a + b % (10**9)
print(sum(dp[n]) % (10**9))
