import sys

input = sys.stdin.readline

n, k = map(int, input().split())

rs = []
check = [False] * (n + 1)


def back(n, k):
    if k == 0:
        print(" ".join(map(str, rs)))

    for i in range(1, n + 1):
        if not check[i]:
            for j in range(1, i + 1):
                check[j] = True
            rs.append(i)
            back(n, k - 1)
            rs.pop()
            for j in range(1, i + 1):
                check[j] = False


back(n, k)
