from collections import deque
def bfs(maps):
    rows = len(maps)
    columns = len(maps[0])
    visited = [[False] * columns for _ in range(rows)]
    
    que = deque()
    count = 1
    que.append((0,0, count))
    visited[0][0] = True
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    
    flag = False
    
    while que:
        y,x,distance = que.popleft()
        count = distance
        if y == rows - 1 and x == columns - 1:
            flag = True
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < rows and 0 <= nx < columns:
                if maps[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    que.append((ny,nx,distance + 1))
        
    return count if flag else -1
        

def solution(maps):
    return bfs(maps)
    
    