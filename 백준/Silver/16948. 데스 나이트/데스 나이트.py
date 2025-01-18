import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [int(i) for i in input().split()]

r1, c1, r2, c2 = arr

visited = set()

d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]


def bfs():
    que = deque()
    que.append((r1, c1, 0))
    visited.add((r1, c1))

    while que:
        r, c, cnt = que.popleft()

        if r == r2 and c == c2:
            return cnt

        for dr, dc in d:
            nr = r + dr
            nc = c + dc

            if nr >= n or nr < 0 or nc >= n or nc < 0 or (nr, nc) in visited:
                continue

            visited.add((nr, nc))
            que.append((nr, nc, cnt + 1))

    return -1


def main():
    return bfs()


print(main())
