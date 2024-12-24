import sys
from collections import deque

input = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def main(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    que = deque()
    visited[0][0] = True
    que.append((0, 0, 1))
    
    while que:
        y, x, cnt = que.popleft()
        
        if y == len(maps) - 1 and x == len(maps[0]) - 1:
            return cnt
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == "1" and not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))
                
    
    return -1
    

n,m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(input().strip()))
    
print(main(maps))
    

    