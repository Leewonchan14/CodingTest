import sys

from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())


def bfs():
    global f, s, g, u, d
    que = deque([(s, 0)])
    visited = set([s])

    while que:
        s, cnt = que.popleft()

        if s == g:
            return cnt

        for ns in [s + u, s - d]:
            if 1 <= ns <= f and ns not in visited:
                visited.add(ns)
                que.append((ns, cnt + 1))

    return "use the stairs"


def main():
    print(bfs())


main()
