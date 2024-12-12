import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline
tc = int(input())
li = [(int(input()), int(input())) for _ in range(tc)]

dp = [[0] * 15 for _ in range(15)]


def recursion(k, n):
    if k == 0:
        return n

    if dp[k][n] == 0:
        cnt = 0
        for i in range(1, n + 1):
            cnt += recursion(k - 1, i)

        dp[k][n] = cnt

    return dp[k][n]


for kk, nn in li:
    print(recursion(kk, nn))

# print(recursion(1, 3))
