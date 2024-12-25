import sys
from collections import deque

input = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def main(maps):
    weights = [[float("inf")] * len(maps[0]) for _ in range(len(maps))]
    que = deque()
    que.append((0, 0, 0, 0))
    min_wall = float("inf")

    while que:
        y, x, cnt, wall = que.popleft()

        if y == len(maps) - 1 and x == len(maps[0]) - 1:
            min_wall = min(min_wall, wall)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                nw = wall
                if maps[ny][nx] != 0:
                    nw += 1

                if nw >= weights[ny][nx]:
                    continue

                weights[ny][nx] = nw
                que.append((ny, nx, cnt + 1, nw))

    return min_wall


n, m = map(int, input().split())
maps = [[int(i) for i in input().strip()] for _ in range(m)]

print(main(maps))
