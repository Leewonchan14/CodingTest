import sys

input = sys.stdin.readline


def isGoodPoint(maps, y, x):
    return 0 <= y < len(maps) and 0 <= x < len(maps[0])


woo = [(0, -1), (0, 1), (-1, 0), (1, 0)]

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def recur4(maps, y, x, cnt, visited, sumv, maxv):
    if cnt == 4:
        maxv = max(maxv, sumv)
        return maxv

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not isGoodPoint(maps, ny, nx) or visited[ny][nx]:
            continue

        visited[ny][nx] = True
        maxv = recur4(maps, ny, nx, cnt + 1, visited, sumv + maps[ny][nx], maxv)
        visited[ny][nx] = False

    return maxv


def getWoo(maps, y, x):
    maxv = 0
    for i in range(4):
        notwoo = [w for w in woo if w != woo[i]]

        li = [maps[y][x]]
        for nw in notwoo:
            ny = y + nw[0]
            nx = x + nw[1]
            if not isGoodPoint(maps, ny, nx):
                continue

            li.append(maps[ny][nx])

        maxv = max(maxv, sum(li))

    return maxv


def main(maps):
    maxv = 0
    visited = [[False] * len(maps[r]) for r in range(len(maps))]
    for r in range(len(maps)):
        for c in range(len(maps[r])):
            visited[r][c] = True
            a = recur4(maps, r, c, 1, visited, maps[r][c], 0)
            visited[r][c] = False
            b = getWoo(maps, r, c)
            maxv = max(maxv, a, b)

    return maxv


r, c = map(int, input().split())
maps = []
for i in range(r):
    maps.append([int(j) for j in input().split()])

print(main(maps))
