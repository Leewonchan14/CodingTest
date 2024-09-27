n = int(input())

dp = [-1, -1, -1, 1, -1, 1]

for i in range(6, n + 1):
    if dp[i - 5] > 0 and dp[i - 3] > 0:
        dp.append(min(dp[i - 5], dp[i - 3]) + 1)
    elif dp[i - 5] > 0 or dp[i - 3] > 0:
        dp.append(max(dp[i - 5], dp[i - 3]) + 1)
    else:
        dp.append(-1)
print(dp[n])