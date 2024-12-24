import sys

from collections import deque


def get_d(x):
    return [-1, 1, x]


def main(n, k):
    g = {}
    visited = [False] * (10**5 + 1)
    que = deque()
    que.append([n, 0])
    visited[n] = True

    while que:
        s, cnt = que.popleft()

        if s == k:
            break

        for d in get_d(s):
            nn = s + d

            if 0 <= nn < len(visited) and not visited[nn]:
                visited[nn] = True
                g[nn] = s
                que.append([nn, cnt + 1])

    li = [k]
    while li[-1] in g:
        li.append(g[li[-1]])

    li.reverse()

    return [cnt, li]


n, k = map(int, input().split())
cnt, li = main(n, k)
print(cnt)
print(" ".join([str(i) for i in li]))
