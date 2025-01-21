import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [[int(i) for i in input().strip()] for _ in range(n)]
dic = [[[0] for _ in range(m)] for _ in range(n)]

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def inner(y, x):
    return 0 <= y < n and 0 <= x < m


def bfs(y, x, visited):
    cnt_li = [1]
    que = deque([(y, x)])
    dic[y][x] = cnt_li
    visited[y][x] = True

    while que:
        y, x = que.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if inner(ny, nx) and maps[ny][nx] == 0 and not visited[ny][nx]:
                cnt_li[0] += 1
                visited[ny][nx] = True
                dic[ny][nx] = cnt_li
                que.append((ny, nx))

    dic[y][x][0] %= 10


def main():
    visited = [[False] * m for _ in range(n)]
    new_maps = [[0] * m for _ in range(n)]

    for r in range(n):
        for c in range(m):
            if maps[r][c] == 0 and not visited[r][c]:
                bfs(r, c, visited)

    for r in range(n):
        for c in range(m):
            if maps[r][c] == 1:
                adj_li = [[0], [0], [0], [0]]
                for i in range(4):
                    nr, nc = r + dy[i], c + dx[i]
                    if inner(nr, nc) and maps[nr][nc] == 0:
                        if any([dic[nr][nc] is a_li for a_li in adj_li]):
                            continue
                        adj_li[i] = dic[nr][nc]
                new_maps[r][c] = (sum([cnt_li[0] for cnt_li in adj_li]) + 1) % 10

    for r_li in new_maps:
        print("".join(map(str, r_li)))


main()
