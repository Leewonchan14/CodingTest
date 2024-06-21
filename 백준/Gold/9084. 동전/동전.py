import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n = int(input())
    ls = list(map(int, input().split()))
    k = int(input())
    dp = [0] * (k + 1)
    dp[0] = 1  # 0원을 만드는 경우의 수는 1개

    for coin in ls:
        for j in range(coin, k + 1):
            dp[j] += dp[j - coin]

    print(dp[k])