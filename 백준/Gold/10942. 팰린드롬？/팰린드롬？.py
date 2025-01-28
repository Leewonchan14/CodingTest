import sys

sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

n = int(input())
maps = list(map(int, input().split()))
costs = [[False] * (n + 1) for _ in range(n)]

cache = {}


for e in range(1, n + 1):
    for s in range(e - 1, -1, -1):
        costs[s][e] = maps[s] == maps[e -
                                      1] and (s + 1 >= e - 1 or costs[s + 1][e - 1])


tc = int(input())
for _ in range(tc):
    a, b = map(int, input().split())
    print(int(costs[a - 1][b]))
