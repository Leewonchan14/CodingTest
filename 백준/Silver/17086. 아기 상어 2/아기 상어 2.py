import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [[int(i) for i in input().split()] for _ in range(n)]

points = []
for r in range(n):
    for c in range(m):
        if maps[r][c] == 1:
            points.append((r, c))

visited = [[float('inf')] * m for _ in range(n)]

d = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]


def inner(y, x):
    return 0 <= y < n and 0 <= x < m


def bfs():
    que = deque()
    for y, x in points:
        que.append((y, x, 0))
        visited[y][x] = 0

    while que:
        y, x, cost = que.popleft()
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if inner(ny, nx) and cost + 1 < visited[ny][nx]:
                visited[ny][nx] = cost + 1
                que.append((ny, nx, cost + 1))

    return max([max(r_li) for r_li in visited])


print(bfs())
