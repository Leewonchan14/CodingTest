import sys

sys.setrecursionlimit(10 ** 6)

dp = {}


def w(a, b, c):
    if (a, b, c) in dp:
        return dp[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        dp[(a, b, c)] = 1
        return 1

    if a > 20 or b > 20 or c > 20:
        dp[(20, 20, 20)] = w(20, 20, 20)
        return dp[(20, 20, 20)]

    if a < b < c:
        dp[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[(a, b, c)]

    dp[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[(a, b, c)]


input = sys.stdin.readline

while True:
    a_, b_, c_ = map(int, input().split())
    if a_ == b_ == c_ == -1:
        break

    print(f"w({a_}, {b_}, {c_}) = {w(a_, b_, c_)}")
