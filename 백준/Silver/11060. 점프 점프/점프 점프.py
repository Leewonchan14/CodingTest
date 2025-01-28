import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
maps = list(map(int, input().split()))
costs = [float('inf')] * (n)
costs[0] = 0

que = deque()
que.append((0, 0))

while que:
    x, cnt = que.popleft()

    for i in range(1, maps[x] + 1):
        nx = x + i
        if nx < n and cnt + 1 < costs[nx]:
            costs[nx] = cnt + 1
            que.appendleft((nx, cnt + 1))

print(costs[-1] if costs[-1] != float('inf') else -1)
