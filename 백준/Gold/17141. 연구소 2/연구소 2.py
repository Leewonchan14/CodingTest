import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [[int(i) for i in input().split()] for _ in range(n)]
can_virus = []

for r in range(n):
    for c in range(n):
        if maps[r][c] == 2:
            can_virus.append((r, c))


def combi():
    result = []
    li = []

    def recur():
        if len(li) == m:
            result.append([can_virus[i] for i in li])
            return

        for i in range(len(can_virus)):
            if not li or i > li[-1]:
                li.append(i)
                recur()
                li.pop()

    recur()
    return result


dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def inner(y, x):
    return 0 <= y < n and 0 <= x < n


def bfs(can):
    visited = [[-1] * n for _ in range(n)]

    for r, c in can:
        visited[r][c] = 0

    que = deque([(r, c, 0) for r, c in can])

    maxv = 0

    while que:
        y, x, cnt = que.popleft()
        maxv = max(maxv, cnt)

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if inner(ny, nx) and (maps[ny][nx] == 0 or maps[ny][nx] == 2) and visited[ny][nx] == -1:
                visited[ny][nx] = cnt + 1
                que.append((ny, nx, cnt + 1))

    for y in range(n):
        for x in range(n):
            if (maps[y][x] == 0 or maps[y][x] == 2) and visited[y][x] == -1:
                return -1

    return maxv


def main():
    result = []
    for can in combi():
        result.append(bfs(can))

    result = [i for i in result if i != -1]
    if result:
        return min(result)

    return -1


print(main())
