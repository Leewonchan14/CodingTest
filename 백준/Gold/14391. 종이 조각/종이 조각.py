def toBit(n, h, w):
    result = []
    bit = ("0" * (h * w) + bin(n)[2:])[-h * w:]
    for hh in range(1, h + 1):
        result.append(list(bit[w * (hh - 1) : w * hh]))

    return result


def listToNum(li):
    return int("".join([str(i) for i in li]))


def calc(bit, maps, h, w):
    sumv = 0
    visited = [[False] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if visited[r][c]:
                continue

            # col
            if bit[r][c] == "1":
                li = []
                i = 0
                while r + i < h and bit[r + i][c] == "1":
                    visited[r + i][c] = True
                    li.append(maps[r + i][c])
                    i += 1

                sumv += listToNum(li)

            # row
            if bit[r][c] == "0":
                li = []
                i = 0
                while c + i < w and bit[r][c + i] == "0":
                    visited[r][c + i] = True
                    li.append(maps[r][c + i])
                    i += 1
                sumv += listToNum(li)

    return sumv


def main(maps):
    maxv = -float("inf")
    h = len(maps)
    w = len(maps[0])
    for i in range(2 ** (h * w)):
        maxv = max(maxv, calc(toBit(i, h, w), maps, h, w))

    return maxv


import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [[int(i) for i in input().strip()] for _ in range(n)]
print(main(maps))
