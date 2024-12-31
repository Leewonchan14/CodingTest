import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(input().strip()) for _ in range(n)]


def find_red_blue():
    ry, rx = 0, 0
    by, bx = 0, 0
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == "R":
                ry, rx = r, c
            elif maps[r][c] == "B":
                by, bx = r, c
    return ry, rx, by, bx


dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def get_n(y, x, i, oy, ox):
    ny = y + dy[i]
    nx = x + dx[i]
    while not (maps[ny][nx] == "#" or maps[ny][nx] == "O") and not (
        ny == oy and nx == ox
    ):
        y = ny
        x = nx
        ny = y + dy[i]
        nx = x + dx[i]

    if maps[ny][nx] == "O":
        return ny, nx

    return y, x


def get_order(i, ry, rx, by, bx):
    if i == 0 or i == 2:
        if (i == 0 and rx < bx) or (i == 2 and rx > bx):
            return "r"
        else:
            return "b"

    else:
        if (i == 1 and ry < by) or (i == 3 and ry > by):
            return "r"
        else:
            return "b"


def bfs():
    ry, rx, by, bx = find_red_blue()
    visited = set()
    visited.add((ry, rx, by, bx))
    que = deque([(ry, rx, by, bx, 0)])
    while que:
        ry, rx, by, bx, cnt = que.popleft()
        if cnt == 10:
            return -1

        for i in range(4):
            order = get_order(i, ry, rx, by, bx)
            if order == "r":
                nry, nrx = get_n(ry, rx, i, by, bx)
                nby, nbx = get_n(by, bx, i, nry, nrx)

            else:
                nby, nbx = get_n(by, bx, i, ry, rx)
                nry, nrx = get_n(ry, rx, i, nby, nbx)

            if maps[nry][nrx] == "O" or maps[nby][nbx] == "O":
                if maps[nby][nbx] == "O":
                    continue

                if maps[nry][nrx] == "O":
                    return cnt + 1

            if (nry, nrx, nby, nbx) in visited:
                continue

            visited.add((nry, nrx, nby, nbx))
            que.append((nry, nrx, nby, nbx, cnt + 1))

    return -1


def main():
    return bfs()


print(main())
