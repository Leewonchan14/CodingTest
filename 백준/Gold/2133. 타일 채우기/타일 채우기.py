import sys

input = sys.stdin.readline


def main(n):
    dp = {2: 3}
    for i in range(4, n + 1, 2):
        sumv = 0
        for j in range(2, i, 2):
            sumv += dp[i - j] * (3 if j == 2 else 2)

        dp[i] = sumv + 2

    if n % 2 == 1:
        return 0

    return dp[n]


print(main(int(input())))
