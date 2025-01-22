import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
maps = [[int(i) for i in input().split()] for _ in range(n)]
yx_fish = [0, 0, [2, 0]]

for r in range(n):
    for c in range(n):
        if maps[r][c] == 9:
            yx_fish[0], yx_fish[1] = r, c

maps[yx_fish[0]][yx_fish[1]] = 0

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]


def inner(y, x):
    return 0 <= y < n and 0 <= x < n


def fish_can_go(y, x, visited):
    if not inner(y, x):
        return False

    if visited[y][x]:
        return False

    if maps[y][x] > yx_fish[2][0]:
        return False

    return True


def can_eat(y, x):
    return maps[y][x] != 0 and maps[y][x] < yx_fish[2][0]


def eat(can):
    can.sort()
    y, x, cnt = can[0]
    yx_fish[0], yx_fish[1] = y, x
    if yx_fish[2][1] + 1 == yx_fish[2][0]:
        yx_fish[2][0], yx_fish[2][1] = yx_fish[2][0] + 1, 0
    else:
        yx_fish[2][1] += 1
    maps[y][x] = 0
    return y, x, cnt


def bfs():
    visited = [[False] * n for _ in range(n)]
    que = deque()
    que.append((yx_fish[0], yx_fish[1], 0))
    pre = 0
    can = []
    visited[yx_fish[0]][yx_fish[1]] = True

    while que:
        y, x, cnt = que.popleft()

        # 거리가 달라졌 && 먹을수 있는 고기가 있다면
        if cnt != pre and can:
            y, x, cnt = eat(can)
            return cnt

        pre = cnt
        if can_eat(y, x):
            can.append((y, x, cnt))

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if fish_can_go(ny, nx, visited):
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))

    if can:
        y, x, cnt = eat(can)
        return cnt

    return None


def main():
    sumv = 0
    while True:
        np = bfs()

        if np == None:
            break

        sumv += np

    print(sumv)


main()
