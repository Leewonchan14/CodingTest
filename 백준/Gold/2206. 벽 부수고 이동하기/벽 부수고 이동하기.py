import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

maps = [[int(i) for i in input().strip()] for _ in range(n)]

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def main():
    que = deque()
    que.append((0, 0, 1))
    lengths = [[[float("inf"), float("inf")] for _ in range(m)] for _ in range(n)]
    lengths[0][0][1] = 1

    while que:
        y, x, chance = que.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 and chance == 0:
                    continue

                n_chance = chance
                if chance == 1 and maps[ny][nx] == 1:
                    n_chance = 0

                # 이전 거보다 작아야 감
                if lengths[y][x][chance] + 1 < lengths[ny][nx][n_chance]:
                    lengths[ny][nx][n_chance] = lengths[y][x][chance] + 1
                    que.append((ny, nx, n_chance))

    if min(lengths[n - 1][m - 1]) == float("inf"):
        return -1

    return min(lengths[n - 1][m - 1])


print(main())
