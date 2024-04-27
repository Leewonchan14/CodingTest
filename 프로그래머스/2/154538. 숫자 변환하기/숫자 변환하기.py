from collections import deque
N = [0]
f1 = lambda v: v + N[0]
f2 = lambda v: v * 2
f3 = lambda v: v * 3
ls = [f1, f2, f3]

def bfs(x, y, n):
    que = deque()
    que.append((x, 0))
    visited = set()
    visited.add(x)
    
    while que:
        nx, cnt = que.popleft()
        if nx == y:
            return cnt
        
        for f in ls:
            ny = f(nx)
            if ny <= y and ny not in visited:
                visited.add(ny)
                que.append((ny, cnt + 1))
    
    return -1
    
    
def solution(x, y, n):
    N[0] = n
    return bfs(x,y,n)
    
        
        