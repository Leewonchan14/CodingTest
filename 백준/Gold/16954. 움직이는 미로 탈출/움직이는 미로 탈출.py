import sys
from collections import deque

input = sys.stdin.readline

maps = [list(input().strip()) for _ in range(8)]
visited = set()
d = []
for i in range(3):
    for j in range(3):
        d.append(([-1, 0, 1][i], [-1, 0, 1][j]))


def inner(y, x):
    return 0 <= y < 8 and 0 <= x < 8


def down():
    for c in range(8):
        cols = deque([maps[r][c] for r in range(8)])
        cols.pop()
        cols.appendleft(".")

        for i in range(8):
            maps[i][c] = cols[i]


def bfs():
    que = deque()
    que.append((7, 0, 0))
    visited.add((7, 0, 0))
    pre_dist = 0

    while que:
        y, x, dist = que.popleft()
        if y == 0 and x == 7:
            return 1

        # 너비 한턴이 끝났다면 벽을 내린다.
        if pre_dist != dist:
            down()
            pre_dist = dist

        # 내려온 벽이 현재 위치라면 넘어간다.
        if maps[y][x] == "#":
            continue

        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if not inner(ny, nx):
                continue

            # 길이 아니라면 넘어간다.
            if maps[ny][nx] == "." and (ny, nx, dist + 1) not in visited:
                visited.add((ny, nx, dist + 1))
                que.append((ny, nx, dist + 1))

    return 0


print(bfs())
