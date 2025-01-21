import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())

maps = [[int(i) for i in input().strip()] for _ in range(n)]
visited = [[[float("inf")] * (k + 1) for _ in range(m)] for _ in range(n)]
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def inner(y, x):
    return 0 <= y < n and 0 <= x < m


def bfs(y, x):
    que = deque()
    que.append((y, x, k))
    visited[y][x][k] = 1

    while que:
        y, x, chance = que.popleft()

        if y == n - 1 and x == m - 1:
            return visited[y][x][chance]

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # 밖이면 넘어가기
            if not inner(ny, nx):
                continue

            # 기회없는데 벽이면 넘어가기
            if chance == 0 and maps[ny][nx] == 1:
                continue

            n_chance = chance
            if maps[ny][nx] == 1:
                n_chance -= 1

            # 가도 크거나 같다면 갈필요 없음
            if visited[y][x][chance] + 1 >= visited[ny][nx][n_chance]:
                continue

            visited[ny][nx][n_chance] = visited[y][x][chance] + 1
            que.append((ny, nx, n_chance))

    return -1


def main():
    return bfs(0, 0)


print(main())
