import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
maps = [list(input().strip()) for _ in range(n)]
coin = []
for r in range(n):
    for c in range(m):
        if maps[r][c] == "o":
            coin.append([r,c])
            
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

def is_out(y, x):
    return not (0 <= y < n and 0 <= x < m)

def is_out_only_one(y1, x1, y2, x2):
    return (is_out(y1, x1) or is_out(y2, x2)) and not (is_out(y1, x1) and is_out(y2, x2))

def is_load(y, x):
    return not is_out(y, x) and maps[y][x] == "."

def is_valid(y1, x1, y2, x2, visited):
    return not is_out(y1, x1) and not is_out(y2, x2) and is_load(y1, x1) and is_load(y2, x2) and (y1, x1, y2, x2) not in visited
    
            
def bfs(y1, x1, y2, x2):
    visited = set()
    que = deque()
    que.append((y1, x1, y2, x2, 0))
    visited.add((y1, x1, y2, x2))
    
    while que:
        y1, x1, y2, x2, cnt = que.popleft()
        if cnt >= 10:
            return -1
        
        for i in range(4):
            ny1 = y1 + dy[i]
            nx1 = x1 + dx[i]
            ny2 = y2 + dy[i]
            nx2 = x2 + dx[i]
            
            if is_out_only_one(ny1, nx1, ny2, nx2):
                return cnt + 1
            
            if is_load(ny1, nx1) and not is_load(ny2, nx2) and (ny1, nx1, y2, x2) not in visited:
                visited.add((ny1, nx1, y2, x2))
                que.append((ny1, nx1, y2, x2, cnt + 1))
                
            if is_load(ny2, nx2) and not is_load(ny1, nx1) and (y1, x1, ny2, nx2) not in visited:
                visited.add((y1, x1, ny2, nx2))
                que.append((y1, x1, ny2, nx2, cnt + 1))
                
            if is_load(ny1, nx1) and is_load(ny2, nx2) and (ny1, nx1, ny2, nx2) not in visited:
                visited.add((ny1, nx1, ny2, nx2))
                que.append((ny1, nx1, ny2, nx2, cnt + 1))
            
    return -1
        

def main():
    print(bfs(*coin[0], *coin[1]))
        
main()