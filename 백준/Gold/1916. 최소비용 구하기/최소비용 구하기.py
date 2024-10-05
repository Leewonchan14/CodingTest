import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

dic = [[] for i in range(n + 1)]
weights = [float('inf')] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    dic[a].append((c, b))
    
a,b = map(int, input().split())

weights[a] = 0
que = [(0, a)]

while que:
    s_w, start = heapq.heappop(que)
    if s_w > weights[start]:
        continue
    
    for e_w, end in dic[start]:
        if s_w + e_w < weights[end]:
            weights[end] = s_w + e_w
            heapq.heappush(que, (weights[end], end))

print(weights[b])