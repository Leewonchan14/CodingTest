import math

dp = [_ for _ in range(10**5 + 1)]

for i in range(1, 10**5 + 1):
    for j in range(1, math.floor(i**0.5) + 1):
        if dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1


def main(n):
    return dp[n]


n = int(input())
print(main(n))
