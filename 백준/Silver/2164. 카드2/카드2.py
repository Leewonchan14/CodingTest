from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

que = deque([i for i in range(1, n + 1)])

while len(que) != 1:
    que.popleft()
    que.append(que.popleft())
    
print(que.popleft())