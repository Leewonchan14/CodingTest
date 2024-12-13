import sys

input = sys.stdin.readline

tc = int(input())

maxv = 10**6
dp = [0] * (maxv + 1)
for i in range(1, maxv + 1):
    for j in range(i, maxv + 1, i):
        dp[j] += i
    dp[i] += dp[i - 1]


def recur(n):
    return dp[n]


for i in range(tc):
    print(recur(int(input())))
