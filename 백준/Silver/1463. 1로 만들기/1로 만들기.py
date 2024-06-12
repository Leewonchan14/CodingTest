import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())

dp = [0, 0]

for i in range(2, N + 1):
    a = dp[i - 1] + 1
    b = dp[i // 2] + 1 if i % 2 == 0 else float('inf')
    c = dp[i // 3] + 1 if i % 3 == 0 else float('inf')
    dp.append(min(a, b, c))

print(dp[N])
