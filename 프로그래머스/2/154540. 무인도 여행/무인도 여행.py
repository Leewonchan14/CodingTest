from collections import deque


def bfs(y, x, visited, maps):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    que = deque()
    que.append((y, x))
    visited[y][x] = True
    cnt = 0

    while que:
        y, x = que.popleft()
        cnt += int(maps[y][x])

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < len(maps) and 0 <= nx < len(maps[ny]):
                if not visited[ny][nx] and maps[ny][nx] != "X":
                    visited[ny][nx] = True
                    que.append((ny, nx))

    return cnt


def solution(maps):
    visited = [[False] * len(i) for i in maps]
    maps = list(map(lambda x: list(x), maps))

    rs = []

    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if not visited[y][x] and maps[y][x] != "X":
                rs.append(bfs(y, x, visited, maps))

    rs.sort()

    return rs if rs else [-1]

