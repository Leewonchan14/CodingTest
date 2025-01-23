import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())
n, m = 0, 0
maps = []
people = []


def input_case():
    global n, m, maps, people
    n, m = map(int, input().split())
    maps = [["."] * (m + 2)]
    for _ in range(n):
        maps.append([".", *list(input().strip()), "."])
    maps.append(["."] * (m + 2))

    n += 2
    m += 2

    people = [(0, 0)]
    for r in range(1, n - 1):
        for c in range(1, m - 1):
            if maps[r][c] == "$":
                people.append((r, c))


dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def inner(y, x):
    return 0 <= y < n and 0 <= x < m


def bfs(y, x):
    global n, m, maps, people
    que = deque([(y, x, 0)])
    visited = [[float('inf')] * m for _ in range(n)]
    visited[y][x] = 0

    while que:
        y, x, hit = que.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if inner(ny, nx) and maps[ny][nx] != "*":
                # 길인경우 그냥간다.
                if (maps[ny][nx] == "." or maps[ny][nx] == "$") and hit < visited[ny][nx]:
                    visited[ny][nx] = hit
                    que.append((ny, nx, hit))

                # 문인경우 부순다.
                if maps[ny][nx] == "#" and hit + 1 < visited[ny][nx]:
                    visited[ny][nx] = hit + 1
                    que.append((ny, nx, hit + 1))

    return visited


def main():
    global n, m, maps, people
    for _ in range(tc):
        input_case()
        coasts = [[0] * m for _ in range(n)]
        for y, x in people:
            visited = bfs(y, x)

            # for r_li in visited:
            #     print(r_li)

            for r in range(n):
                for c in range(m):
                    coasts[r][c] += visited[r][c]

        minv = float('inf')
        for r in range(n):
            for c in range(m):
                if maps[r][c] == "#":
                    coasts[r][c] -= 2

                minv = min(minv, coasts[r][c])

        print(minv)


main()
