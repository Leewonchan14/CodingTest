# dfs 를 하는데 2개이상의 인접 노드가 있다면 3을 리턴한다.

import sys

sys.setrecursionlimit(10**9)

n = int(input())
maps = [list(input().strip()) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]
minv = 0

d = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1)]


def isIn(y, x):
    return 0 <= y < n and 0 <= x < n


def adj(y, x):
    return [(y + ny, x + nx) for ny, nx in d if isIn(y + ny, x + nx)]


def getVisitAdj(y, x):
    return [(ny, nx) for ny, nx in adj(y, x) if visited[ny][nx] >= 0]


def getColor(y, x):
    li = list(set([visited[ny][nx] for ny, nx in getVisitAdj(y, x)]))
    li.sort()
    for i, v in enumerate(li):
        if i != v:
            return i

    return len(li)


cnt = 0


def dfs(sy, sx):
    visited[sy][sx] = getColor(sy, sx)

    def recur(y, x):
        for ny, nx in adj(y, x):
            if maps[ny][nx] == "X" and visited[ny][nx] == -1:
                visited[ny][nx] = getColor(ny, nx)
                recur(ny, nx)

    recur(sy, sx)


def main():
    for r in range(n):
        for c in range(n):
            if visited[r][c] == -1 and maps[r][c] == "X":
                dfs(r, c)

    return min(max([max(r) for r in visited]) + 1, 3)


print(main())
