from collections import deque

def bfs(y, x, maps):
    que = deque()
    n = len(maps) - 1
    m = len(maps[0]) - 1
    que.append((y, x, 1))
    dy = [0,-1,0,1]
    dx = [1,0,-1,0]
    visited = [[False] * (m + 1) for _ in range(n + 1)]
    visited[y][x] = True
    while que:
        y, x, count = que.popleft()
        
        if y == n and x == m:
            return count
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<=n and 0<=nx<=m and maps[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny,nx,count + 1))
                
    return -1
    
    

def solution(maps):
    return bfs(0, 0, maps)
    