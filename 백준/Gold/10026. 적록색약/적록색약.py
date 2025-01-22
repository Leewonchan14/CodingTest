import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
maps = [list(input().strip()) for _ in range(n)]


def inner(y, x):
    return 0 <= y < n and 0 <= x < n


dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]


def bfs(y, x, visited, is_same_color):
    visited[y][x] = True
    que = deque([(y, x)])
    while que:
        y, x = que.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if inner(ny, nx) and is_same_color(maps[y][x], maps[ny][nx]) and not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx))


def main():
    def is_same1(a, b):
        return a == b

    def is_same2(a, b):
        if (a == "R" or a == "G") and (b == "R" or b == "G"):
            return True

        return a == b

    func = [is_same1, is_same2]
    li = []
    for fn in func:
        cnt = 0
        visited = [[False] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if not visited[r][c]:
                    cnt += 1
                    bfs(r, c, visited, fn)
        li.append(cnt)

    print(*li)


main()
