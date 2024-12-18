dp = [[], [1, 0, 0], [0, 1, 0], [1, 1, 1], [2, 0, 1]]


def main(n):
    if n < len(dp):
        return sum(dp[n]) % 1000000009


    for i in range(len(dp), n + 1):
        a = (dp[i - 1][1] + dp[i - 1][2]) % 1000000009
        b = (dp[i - 2][0] + dp[i - 2][2]) % 1000000009
        c = (dp[i - 3][0] + dp[i - 3][1]) % 1000000009
        dp.append([a, b, c])

    return sum(dp[n]) % 1000000009


import sys

input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    print(main(int(input())))
