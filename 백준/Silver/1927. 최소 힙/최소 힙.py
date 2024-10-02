import sys
from queue import PriorityQueue
input = sys.stdin.readline

que = PriorityQueue()

for _ in range(int(input())):
    n = int(input())

    if n == 0:
        print(0 if not que.queue else que.get())
    else:
        que.put(n)

        