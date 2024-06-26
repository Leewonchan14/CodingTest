import sys

input = sys.stdin.readline

n, m, k, = map(int, input().split())

li = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]

r = 0

for i in range(1, n + 1):
    for c in range(1, m + 1):
        for g in range(1, k + 1):
            n_c, n_g = li[i - 1]

            if c >= n_c and g >= n_g:
                dp[i][c][g] = max(dp[i - 1][c][g], dp[i - 1][c - n_c][g - n_g] + 1)

            else:
                dp[i][c][g] = dp[i - 1][c][g]

            r = max(r, dp[i][c][g])

print(r)
