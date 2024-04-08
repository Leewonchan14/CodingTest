from collections import deque


def bfs(visited, rectangle, start, end, maxv):
    y, x = start
    que = deque()
    que.append((y, x, 0))

    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]

    while que:
        y, x, count = que.popleft()
        if end[0] == y and end[1] == x:
            return count
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (0 <= ny <= maxv and 0 <= nx <= maxv and not visited[ny][nx] and
                    ok_go(rectangle, (ny, nx)) and
                    ok_go(rectangle, ((y + ny) / 2, (x + nx) / 2))):
                visited[ny][nx] = True
                que.append((ny, nx, count + 1))


def ok_go(rectangle, target):
    y, x = target
    for ld_x, ld_y, ry_x, ry_y in rectangle:
        if ((x == ld_x or x == ry_x) and ld_y <= y <= ry_y) or ((y == ld_y or y == ry_y) and ld_x <= x <= ry_x):
            if not any((y1 < y < y2 and x1 < x < x2) for x1, y1, x2, y2 in rectangle):
                return True

    return False


def solution(rectangle, characterX, characterY, itemX, itemY):
    start = characterY, characterX
    end = itemY, itemX
    maxv = 0
    for i in rectangle:
        maxv = max(max(i), maxv)

    visited = [[False] * (maxv + 1) for _ in range(maxv + 1)]
    return bfs(visited, rectangle, start, end, maxv)
