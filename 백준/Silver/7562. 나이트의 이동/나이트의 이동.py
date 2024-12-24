import sys
from collections import deque

d = []

def set_d():
    li = []
    def recur():
        if len(li) == 2 and abs(li[0]) == abs(li[1]):
            return
        
        if len(li) == 2:
            d.append(li[:])
            return
        
        for i in [2,1,-1,-2]:
            if i not in li:
                li.append(i)
                recur()
                li.pop()
                
    recur()


def main(start, end, k):
    visited = [[False] * k for _ in range(k)]
    
    que = deque()
    que.append((*start, 0))
    
    while que:
        y, x, cnt = que.popleft()
        
        if y == end[0] and x == end[1]:
            return cnt
        
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            
            if 0 <= ny < k and 0 <= nx < k and not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny, nx, cnt + 1))
            



input = sys.stdin.readline

tc = int(input())
set_d()

for _ in range(tc):
    k = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    
    print(main((sy, sx),(ey, ex), k))