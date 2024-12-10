from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def isCorrectPoint(y, x, maps, visited):
    return (
        0 <= y < len(maps)
        and 0 <= x < len(maps[0])
        and maps[y][x] != "X"
        and not visited[y][x]
    )


def bfs(maps, start, end):
    visited = [[False] * len(r) for r in maps]
    visited[start[0]][start[1]] = True
    que = deque([(*start, 0)])

    while que:
        y, x, c = que.popleft()
        if end[0] == y and end[1] == x:
            return c

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not isCorrectPoint(ny, nx, maps, visited):
                continue

            visited[ny][nx] = True
            que.append((ny, nx, c + 1))

    return -1


def solution(maps):
    start = 0
    lever = 0
    end = 0
    for r in range(len(maps)):
        for c in range(len(maps[r])):
            if maps[r][c] == "S":
                start = (r, c)
            if maps[r][c] == "L":
                lever = (r, c)
            if maps[r][c] == "E":
                end = (r, c)

    a = bfs(maps, start, lever)
    if a == -1:
        return -1

    b = bfs(maps, lever, end)
    if b == -1:
        return -1
    return a + b
