import sys

input = sys.stdin.readline

n = int(input())
maps = [[int(i) for i in input().split()] for _ in range(n)]


def comibiH(n, k):
    li = []
    result = []

    def recur():
        if len(li) == k:
            result.append(li[:])
            return

        for i in range(n):
            li.append(i)
            recur()
            li.pop()

    recur()
    return result


def compact(li):
    comp = [c for c in li if c != 0]
    for i in range(len(comp) - 1):
        if comp[i] == comp[i + 1]:
            comp[i] *= 2
            comp[i + 1] = 0
    comp = [c for c in comp if c != 0]

    return comp + ([0] * (len(li) - len(comp)))


def flip(maps):
    return [[maps[r][c] for r in range(len(maps))] for c in range(len(maps[0]))]


def left(maps):
    return [compact(r) for r in maps]


def right(maps):
    return [compact(r[::-1])[::-1] for r in maps]


def up(maps):
    return flip(left(flip(maps)))


def down(maps):
    return flip(right(flip(maps)))


funcs = [up, right, down, left]


def main():
    maxv = 0
    for li in comibiH(4, 5):
        n_maps = [r[:] for r in maps]
        for i in li:
            n_maps = funcs[i](n_maps)

        maxv = max(maxv, max([max(r) for r in n_maps]))

    return maxv


print(main())
