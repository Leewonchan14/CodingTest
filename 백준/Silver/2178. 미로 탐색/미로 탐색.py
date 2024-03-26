"""
bfs 로 가장 먼저 도착 했을때 값을 리턴
def bfs(v)
v : (y,x)

visited = bool[][]

Queue[(y,x),cnt]
cnt : int
"""

import sys
from collections import deque


def bfs(n, m, v, maped):
    visited = [[False] * m for _ in range(n)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    y, x = v
    que = deque()
    visited[y][x] = True
    que.append((y, x, 1))

    while que:
        y, x, cnt = que.popleft()

        if y + 1 == n and x + 1 == m:
            return cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and maped[ny][nx] == 1:
                    visited[ny][nx] = True
                    que.append((ny, nx, cnt + 1))


input = sys.stdin.readline

n, m = map(int, input().split())

maped = [list(map(int, list(input().split()[0]))) for _ in range(n)]

print(bfs(n, m, (0, 0), maped))
