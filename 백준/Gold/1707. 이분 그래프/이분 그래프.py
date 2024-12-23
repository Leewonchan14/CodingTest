import sys
from collections import deque

input = sys.stdin.readline


def main(dic, n):
    visited = [set(), set()]

    def bfs():
        for first in [i for i in dic.keys() if len(dic[i]) > 0]:
            if first in visited[0] or first in visited[1]:
                continue
            que = deque()
            visited[0].add(first)
            que.append((first, 0))

            while que:
                start, now_visited = que.popleft()
                for nn in dic[start]:
                    if nn in visited[now_visited % 2]:
                        return False

                    if nn in visited[(now_visited + 1) % 2]:
                        continue

                    visited[(now_visited + 1) % 2].add(nn)
                    que.append((nn, now_visited + 1))

        return True

    if not bfs():
        print("NO")
    else:
        print("YES")


tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    dic = {i + 1: [] for i in range(n)}
    for _ in range(m):
        a, b = map(int, input().split())
        dic[a].append(b)
        dic[b].append(a)

    main(dic, n)
