import sys
from collections import deque

input = sys.stdin.readline
tu = tuple([input().split() for _ in range(3)])
tu = tuple(("" if t[0] == "0" else t[1]) for t in tu)
visited = set()


def bfs():
    global tu
    que = deque()
    que.append((tu, 0))
    visited.add(tu)

    while que:
        tu, cnt = que.popleft()

        if all([all([j == "ABC"[i] for j in tu[i]]) for i in range(3)]):
            return cnt

        for i in range(3):
            for j in range(3):
                if i == j or tu[i] == "":
                    continue

                n_li = list(tu)
                n_li[j] = n_li[j] + n_li[i][-1]
                n_li[i] = n_li[i][:-1]

                n_tu = tuple(n_li)

                if n_tu not in visited:
                    visited.add(n_tu)
                    que.append((n_tu, cnt + 1))


def main():
    print(bfs())


main()
