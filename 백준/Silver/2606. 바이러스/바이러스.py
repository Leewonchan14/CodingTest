import sys

input = sys.stdin.readline

from collections import deque

n = int(input())

m = int(input())

maped = {}

for i in range(m):
    a, b = map(int, input().split())
    relation = maped.get(a, [])
    relation.append(b)
    maped[a] = relation

    relation = maped.get(b, [])
    relation.append(a)
    maped[b] = relation


def bfs(v: int, maped, n):
    cnt = 0
    que = deque()
    visited = {i + 1: False for i in range(n)}
    que.append(v)
    visited[v] = True
    while que:
        key = que.popleft()
        cnt += 1

        relation = maped.get(key, [])

        for item in relation:
            if not visited[item]:
                visited[item] = True
                que.append(item)

    return cnt - 1

print(bfs(1, maped, n))
