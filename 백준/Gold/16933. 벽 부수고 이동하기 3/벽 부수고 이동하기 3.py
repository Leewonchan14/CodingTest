import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())

maps = [[int(i) for i in input().strip()] for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def inner(y, x):
    return 0 <= y < n and 0 <= x < m


def bfs(y, x):
    que = deque()
    que.append((y, x, 1, k, 1))
    visited[y][x][k] = 1

    while que:
        y, x, dist, chance, dayNight = que.popleft()

        if y == n - 1 and x == m - 1:
            return dist

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not inner(ny, nx):
                continue

            # 길이면 그냥 간다.
            if maps[ny][nx] == 0 and visited[ny][nx][chance] == 0:
                visited[ny][nx][chance] = dist + 1
                que.append((ny, nx, dist + 1, chance, 1 - dayNight))
                continue

            # 벽인데
            if maps[ny][nx] == 1 and chance > 0 and visited[ny][nx][chance - 1] == 0:
                # 낮인경우 부수고 간다.
                if dayNight:
                    visited[ny][nx][chance - 1] = dist + 1
                    que.append((ny, nx, dist + 1, chance - 1, 1 - dayNight))

                # 밤인경우 기다린다.
                else:
                    que.append((y, x, dist + 1, chance, 1 - dayNight))

    return -1


def main():
    print(bfs(0, 0))


main()
