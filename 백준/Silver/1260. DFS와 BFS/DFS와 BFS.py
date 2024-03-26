import sys
from collections import deque

input = sys.stdin.readline

"""
map = {vertax : sorted (int[]) } 
"""

n, m, v = map(int, input().split())

maped = {}


def bfs(v, maped):
    visited = {i + 1: False for i in range(n)}
    rst = []
    que = deque()

    visited[v] = True
    que.append(v)

    while que:
        key = que.popleft()
        rst.append(key)
        relation = maped.get(key, [])

        for item in relation:
            if not visited[item]:
                visited[item] = True
                que.append(item)

    return " ".join(map(str, rst))


def dfs(v, maped):
    visited = {i + 1: False for i in range(n)}
    rst = []
    stk = [v]

    while stk:
        key = stk.pop()
        if visited[key]:
            continue
        rst.append(key)
        visited[key] = True
        relation = maped.get(key, [])
        relation.sort()

        for i in range(len(relation) - 1, -1, -1):
            if not visited[relation[i]]:
                stk.append(relation[i])

    return " ".join(map(str, rst))


# 간선 입력받기
for i in range(m):
    a, b = map(int, input().split())
    relation = maped.get(a, [])
    relation.append(b)
    maped[a] = relation

    relation = maped.get(b, [])
    relation.append(a)
    maped[b] = relation

print(dfs(v, maped))
print(bfs(v, maped))
