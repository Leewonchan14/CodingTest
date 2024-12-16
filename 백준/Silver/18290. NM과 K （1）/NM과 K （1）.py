import sys

input = sys.stdin.readline


def isGoodPoint(y, x, maps):
    return 0 <= y < len(maps) and 0 <= x < len(maps[0])


def getAdj(y, x, maps, visited):
    li = [(y, x)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if isGoodPoint(ny, nx, maps) and not visited[ny][nx]:
            li.append((ny, nx))

    return li


def checkVisitedAdj(li, visited, bool):
    for y, x in li:
        visited[y][x] = bool


def recur(maps, visited, k, li, maxv, sumv):
    if len(li) == k:
        maxv = max(maxv, sumv)
        return maxv

    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if li:
                lr, lc = li[-1]
                col = len(maps[0])
                if r * col + c <= lr * col + lc:
                    continue

            if isGoodPoint(r, c, maps) and not visited[r][c]:
                adjs = getAdj(r, c, maps, visited)
                checkVisitedAdj(adjs, visited, True)
                li.append((r, c))
                maxv = recur(maps, visited, k, li, maxv, sumv + maps[r][c])
                li.pop()
                checkVisitedAdj(adjs, visited, False)

    return maxv


def main(k, maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    maxv = recur(maps, visited, k, [], -float("inf"), 0)
    print(maxv)


n, m, k = map(int, input().split())
maps = [[int(i) for i in input().split()] for _ in range(n)]

main(k, maps)
