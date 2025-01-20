import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [[int(i) for i in input().split()] for _ in range(n)]

area = []
for r in range(n):
    for c in range(m):
        if maps[r][c] != 0:
            continue
        area.append((r, c))


def combi3(arr):
    result = []
    li = []

    def recur():
        if len(li) == 3:
            result.append(set(arr[i] for i in li))
            return

        for i in range(len(arr)):
            if not li or i > li[-1]:
                li.append(i)
                recur()
                li.pop()

    recur()
    return result


dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def bfs(maps, y, x):
    que = deque()
    que.append((y, x))
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 0:
                maps[ny][nx] = 2
                que.append((ny, nx))


def do_virus(w3):
    new_maps = [r[:] for r in maps]

    for r, c in w3:
        new_maps[r][c] = 1

    for r in range(n):
        for c in range(m):
            if new_maps[r][c] == 2:
                bfs(new_maps, r, c)

    return len([c for r in new_maps for c in r if c == 0])


def main():
    walls3 = combi3(area)
    maxv = 0
    for w3 in walls3:
        maxv = max(maxv, do_virus(w3))

    return maxv


print(main())
