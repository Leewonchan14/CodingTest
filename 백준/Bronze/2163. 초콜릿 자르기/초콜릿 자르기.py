import sys

sys.setrecursionlimit(10**9)


def recur(x, y, cnt):
    if x == 1 and y == 1:
        return 0

    cnt = 0
    if x > y:
        cnt = recur(x // 2, y, cnt) + recur(x - x // 2, y, cnt) + 1
    else:
        cnt = recur(y // 2, x, cnt) + recur(y - y // 2, x, cnt) + 1

    return cnt


a, b = [int(i) for i in input().split()]
print(recur(a, b, 0))

# print(recur(3, 2, 0))
