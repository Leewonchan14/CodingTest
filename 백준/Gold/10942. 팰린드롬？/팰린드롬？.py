import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n = int(input())
maps = list(map(int, input().split()))
costs = [[False] * (n + 1) for _ in range(n)]

cache = {}


def isPelin(s, e):
    key = (s, e)
    if (key in cache):
        return cache[key]

    if s > e:
        return True

    if maps[s] != maps[e - 1]:
        cache[key] = False
        return False

    v = isPelin(s + 1, e - 1)
    cache[key] = v
    return v


for e in range(1, n + 1):
    for s in range(e - 1, -1, -1):
        costs[s][e] = isPelin(s, e)


tc = int(input())
for _ in range(tc):
    a, b = map(int, input().split())
    print(int(costs[a - 1][b]))
