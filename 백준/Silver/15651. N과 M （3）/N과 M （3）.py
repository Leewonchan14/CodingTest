import sys

input = sys.stdin.readline

n, k = map(int, input().split())

rs = []
check = [False] * (n + 1)


def back(n, k1):
    if k1 == 0:
        print(" ".join(map(str, rs)))
        return

    for i in range(1, n + 1):
        rs.append(i)
        back(n, k1 - 1)
        rs.pop()


back(n, k)
