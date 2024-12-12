from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def isGood(y, x, land, visited):
    return (
        0 <= y < len(land)
        and 0 <= x < len(land[0])
        and not visited[y][x]
        and land[y][x] == 1
    )


def dfs(land, visited, start, c_s):
    cnt = 1
    y, x = start
    c_s.add((x))
    visited[y][x] = True

    if x in c_s:
        pass
    else:
        land[y][x] = 0

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not isGood(ny, nx, land, visited):
            continue
        key, c_s = dfs(land, visited, (ny, nx), c_s)
        cnt += key

    return cnt, c_s


def bfs(land, visited, start, c_s):
    y, x = start

    visited[y][x] = True
    que = deque([(y, x)])
    total = 0
    ls = []

    while que:
        y, x = que.popleft()
        total += 1
        if x in c_s:
            land[y][x] = 0
        else:
            c_s.add(x)
            ls.append((y, x))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not isGood(ny, nx, land, visited):
                continue

            visited[ny][nx] = True
            que.append((ny, nx))

    for y, x in ls:
        land[y][x] = total


def solution(land):
    visited = [[False] * len(land[0]) for _ in range(len(land))]

    for r in range(len(land)):
        for c in range(len(land[0])):
            if isGood(r, c, land, visited):
                bfs(land, visited, (r, c), set())

    maxv = 0
    for i in range(len(land[0])):
        maxv = max(sum([land[j][i] for j in range(len(land))]), maxv)

    return maxv

