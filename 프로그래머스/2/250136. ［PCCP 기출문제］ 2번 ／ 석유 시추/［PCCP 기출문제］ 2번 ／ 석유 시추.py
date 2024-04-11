from collections import deque
def bfs(y,x,visited, land):
    que = deque()
    visited[y][x] = True
    count = 0
    
    que.append((y,x,count))
    
    dy = [0,-1,0,1]
    dx = [1,0,-1,0]
    
    c_l = [500, -1]
    
    while que:
        y,x,cnt = que.popleft()
        c_l[0] = min(x, c_l[0])
        c_l[1] = max(x, c_l[1])
        count += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < len(land) and 0 <= nx < len(land[0]):
                if land[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    que.append((ny,nx, cnt + 1))
    
    return count, c_l

def solution(land):
    ls = []
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    for c in range(len(land[0])):
        for r in range(len(land)):
            if land[r][c] == 1 and not visited[r][c]:
                ls.append(bfs(r,c,visited, land))
        
    mm = [0] * len(land[0])
    for cnt, [start, end] in ls:
        for i in range(start, end + 1):
            mm[i] += cnt
    
    return max(mm)