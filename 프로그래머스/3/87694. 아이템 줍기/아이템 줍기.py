from collections import deque


def is_in(y, x, rectangle):
    for lx, ly, rx, ry in rectangle:
        if ly < y < ry and lx < x < rx:
            return True

    return False


def is_side(y, x, rectangle):
    for lx, ly, rx, ry in rectangle:
        if ((x == lx or x == rx) and ly <= y <= ry) or ((y == ly or y == ry) and lx <= x <= rx):
            return True

    return False


dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def bfs(x, y, rectangle, target, visited):
    que = deque()
    que.append((y, x, 0))
    visited[y][x] = True
    n = len(visited) - 1

    while que:
        y, x, cnt = que.popleft()
        print(y, x, cnt)
        if y == target[0] and x == target[1]:
            return cnt

        if y == 5 and cnt == 3:
            print(y)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx <= n and 0 <= ny <= n and not visited[ny][nx]:
                if (
                        is_side(ny, nx, rectangle) and is_side((y + ny) / 2, (x + nx) / 2, rectangle) and
                        not is_in(ny, nx, rectangle) and not is_in((y + ny) / 2, (x + nx) / 2, rectangle)
                ):
                    visited[ny][nx] = True
                    que.append((ny, nx, cnt + 1))


def solution(rectangle, characterX, characterY, itemX, itemY):
    maxv = 0
    for i in rectangle:
        maxv = max(maxv, max(i))

    visited = [[False] * (maxv + 1) for _ in range(maxv + 1)]

    return bfs(characterX, characterY, rectangle, (itemY, itemX), visited)

