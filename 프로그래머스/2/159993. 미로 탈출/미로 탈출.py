from collections import deque

def bfs(y, x, maps, end):
    visited = [[False] * len(i) for i in maps]
    
    dy = [0,1,0,-1]
    dx = [-1,0,1,0]
    
    que = deque()
    visited[y][x] = True
    que.append((y, x, 0))
    while que:
        y,x,count = que.popleft()
        
        if maps[y][x] == end:
            return count
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] \
                and maps[ny][nx] != "X":
                visited[ny][nx] = True
                que.append((ny,nx, count + 1))
                
    return -1
    

def solution(maps):
    s_point = 0,0
    l_point = 0,0
    e_point = 0,0
    
    for row in range(len(maps)):
        for column in range(len(maps[row])):
            if maps[row][column] == "S":
                s_point = row, column
                
            if maps[row][column] == "E":
                e_point = row, column
                
            if maps[row][column] == "L":
                l_point = row, column
                
    sumv = 0
                   
    count = bfs(s_point[0], s_point[1], maps, "L")
    if count == -1:
        return -1
    
    sumv += count
    
    count = bfs(l_point[0], l_point[1], maps, "E")
    
    if count == -1:
        return -1
    
    sumv += count
    
    return sumv
    