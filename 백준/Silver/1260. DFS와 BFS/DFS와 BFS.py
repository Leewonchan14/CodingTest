import sys
from collections import deque

input = sys.stdin.readline


def main(start, dic, n):
    visited = [False] * (n + 1)
    visited[start] = True

    def recur(start):
        print(start, end=" ")
        for nn in dic[start]:
            if visited[nn]:
                continue

            visited[nn] = True
            recur(nn)

    recur(start)
    print()

    visited = [False] * (n + 1)
    visited[start] = True

    def bfs():
        que = deque()
        que.append((start))

        while que:
            s = que.popleft()
            print(s, end=" ")

            for nn in dic[s]:
                if not visited[nn]:
                    visited[nn] = True
                    que.append(nn)

    bfs()


n, tc, start = map(int, input().split())
dic = {i + 1: [] for i in range(n)}
for _ in range(tc):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)


for k in dic.keys():
    dic[k].sort()

main(start, dic, n)
