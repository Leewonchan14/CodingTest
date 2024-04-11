from collections import deque
def bfs(y,x,places):
    visited = [[False] * len(places) for _ in range(len(places))]
    dy = [0,-1,0,1]
    dx = [1,0,-1,0]
    que = deque()
    visited[y][x] = True
    que.append((y,x,0))
    while que:
        y,x,cnt = que.popleft()
        if 1 <= cnt <= 2 and places[y][x] == "P":
            return 0
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < len(places) and 0 <= nx < len(places[0]):
                if not visited[ny][nx] and places[ny][nx] != "X":
                    visited[ny][nx] = True
                    que.append((ny,nx,cnt+1))
        
    return 1

def solution(places):
    ls = []
    for li in places:
        for r in range(len(li)):
            flag = False
            for c in range(len(li[0])):
                rs = bfs(r,c,li)
                if li[r][c] == "P" and rs == 0:
                    ls.append(0)
                    flag = True
                    break
            if flag:
                break
        if not flag:
            ls.append(1)
    
                    
    return ls

    