import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
m, n = map(int, input().split())
maps = [[int(i) for i in input().split()] for _ in range(n)]

d = [(0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]

for i in [-2, -1, 1, 2]:
    for j in [-2, -1, 1, 2]:
        if abs(i) == abs(j):
            continue

        d.append((i, j, 1))


def inner(y, x):
    return 0 <= y < n and 0 <= x < m


def bfs():
    visited = [[[float('inf')] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 0
    que = deque([(0, 0, 0, 0)])

    while que:
        y, x, cnt, kick = que.popleft()

        if y == n - 1 and x == m - 1:
            return cnt

        for dy, dx, is_horse_move in d:
            ny, nx = y + dy, x + dx
            if not inner(ny, nx) or maps[ny][nx] == 1:
                continue

            # 이미 킥 다썼으면
            if is_horse_move and kick == k:
                continue

            if is_horse_move and cnt + 1 < visited[ny][nx][kick + 1]:
                visited[ny][nx][kick + 1] = cnt + 1
                que.append((ny, nx, cnt + 1, kick + 1))

            if not is_horse_move and cnt + 1 < visited[ny][nx][kick]:
                visited[ny][nx][kick] = cnt + 1
                que.append((ny, nx, cnt + 1, kick))

    return -1


print(bfs())
