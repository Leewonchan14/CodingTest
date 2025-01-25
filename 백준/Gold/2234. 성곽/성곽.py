import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt_map = {}

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_d(y, x, isWall):
    v = maps[y][x]
    binary = (("0" * 4) + bin(v)[2:])[-4:]
    return [d[i] for i in range(4) if int(binary[i]) == isWall]


def bfs(y, x, cnt_li):
    que = deque()
    que.append((y, x))
    visited[y][x] = True
    cnt_map[(y, x)] = cnt_li

    cnt = 0

    while que:
        y, x = que.popleft()
        cnt += 1

        for dy, dx in get_d(y, x, 0):
            ny, nx = y + dy, x + dx
            if not visited[ny][nx]:
                visited[ny][nx] = True
                cnt_map[(ny, nx)] = cnt_li
                que.append((ny, nx))

    cnt_li[0] = cnt
    return


def main():
    cnt = 0
    for r in range(n):
        for c in range(m):
            if not visited[r][c]:
                cnt += 1
                cnt_li = [0]
                bfs(r, c, cnt_li)

    print(cnt)
    print(max(sum(cnt_map.values(), [])))

    maxv = 0
    for r in range(n):
        for c in range(m):
            dd = get_d(r, c, 1)
            for dy, dx in dd:
                ny, nx = r + dy, c + dx
                if (ny, nx) in cnt_map and not cnt_map[(ny, nx)] is cnt_map[(r, c)]:
                    maxv = max(maxv, cnt_map[(ny, nx)][0] + cnt_map[(r, c)][0])

    print(maxv)


main()
