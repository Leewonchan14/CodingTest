import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())
k = int(input())

dic = {i:[] for i in range(n + 1)}

for _ in range(e):
    a,b,c = map(int, input().split())
    dic[a].append((c, b))

road = [float('inf')] * (n + 1)
road[k] = 0

que = [(road[k], k)]

while que:
    now_w, start = heapq.heappop(que)
    for w, end in dic.get(start, []):
        if now_w + w < road[end]:
            road[end] = now_w + w
            heapq.heappush(que, (road[end], end))

for i in range(1, n + 1):
    print(road[i] if road[i] != float('inf') else 'INF')