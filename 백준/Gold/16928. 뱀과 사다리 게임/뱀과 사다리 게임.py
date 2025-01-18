import  sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
visited = [False] * (101)

ladder = {}
snake = {}

for _ in range(n):
    a,b = map(int, input().split())
    ladder[a] = b
    
for _ in range(m):
    a,b = map(int, input().split())
    snake[a] = b
    
def bfs():
    que = deque()
    que.append((1, 0))
    visited[1] = True
    
    while que:
        x, cnt = que.popleft()
        
        if x == 100:
            return cnt
        
        for i in range(1, 7):
            nx = x + i
            if nx > 100 or visited[nx]:
                continue
                
            if nx in ladder:
                nx = ladder[nx]
                
            elif nx in snake:
                nx = snake[nx]
                
            visited[nx] = True
            que.append((nx, cnt + 1))
                
    
    
def main():
    return bfs()

print(main())
