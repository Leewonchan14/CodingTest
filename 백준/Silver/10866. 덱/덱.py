import sys
from collections import deque

input = sys.stdin.readline
que = deque()

n = int(input())

for _ in range(n):
    arr = input().split()
    
    if arr[0] == "push_front":
        que.appendleft(arr[1])
    elif arr[0] == "push_back":
        que.append(arr[1])
    elif arr[0] == "pop_front":
        print(-1 if not que else que.popleft())
    elif arr[0] == "pop_back":
        print(-1 if not que else que.pop())
    elif arr[0] == "size":
        print(len(que))
    elif arr[0] == "empty":
        print(1 if not que else 0)
    elif arr[0] == "front":
        print(que[0] if que else -1)
    elif arr[0] == "back":
        print(que[-1] if que else -1)
        
        