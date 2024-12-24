import sys

from collections import deque

def find_one(maps):
    result = []
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 1:
                result.append((r, c))
                
    return result

def is_any_zero(maps):
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 0:
                return True
            
    return False

dy = [0, -1, 0 ,1]
dx = [-1, 0, 1, 0]

def main(maps):
    maxv = 0
    que = deque([(*f, 0) for f in find_one(maps)])
    while que:
        y, x, cnt = que.popleft()
        maxv = max(cnt, maxv)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 0:
                maps[ny][nx] = 1
                que.append((ny, nx, cnt + 1))
                
    if is_any_zero(maps):
        return -1
    
    return maxv
        

input = sys.stdin.readline

n,m = map(int, input().split())
maps = []
for _ in range(m):
    maps.append([int(i) for i in input().split()])
    
print(main(maps))