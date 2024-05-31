buffer = 0
cnt = 0
import sys

input = sys.stdin.readline

n = int(input())

# 처음에 그리디 문제 인줄
dp = [0] * 101

for i in range(7):
    dp[i] = i


def fun(k):
    if k == 0 or dp[k] != 0:
        return dp[k]

    # 1. A 만 붙히는거
    a = fun(k - 1) + 1

    # 2. 1복붙
    b = fun(k - 3) * 2

    # 3. 2복붙
    c = fun(k - 4) * 3

    # 4. 3복붙
    d = fun(k - 5) * 4

    dp[k] = max(a, b, c, d)

    return dp[k]


print(fun(n))
