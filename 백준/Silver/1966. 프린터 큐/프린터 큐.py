import sys
from collections import deque
from queue import PriorityQueue

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    n,m = map(int, input().split())
    li = list(map(int, input().split()))
    que = deque(enumerate(li))
    pq = PriorityQueue()
    for i in li:
        pq.put((1 / i, i))

    cnt = 1

    while pq.queue[0][1] != que[0][1] or que[0][0] != m:
        if pq.queue[0][1] == que[0][1]:
            cnt += 1
            pq.get()
            que.popleft()
            continue
        que.append(que.popleft())

    print(cnt)



