from collections import deque
def get_direction(y,x,board):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    ls = []
    for i in range(4):
        y1 = y
        x1 = x
        while True:
            ny = y1 + dy[i]
            nx = x1 + dx[i]
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and "D" != board[ny][nx]:
                pass
            else:
                break
            y1 = ny
            x1 = nx
            
        ls.append((y1,x1))
        
    return ls
            
            
    

def solution(board):
    start = (0,0)
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "R":
                start = (r,c)
    
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    que = deque()
    que.append((start[0],start[1], 0))
    
    while que:
        y,x, cnt = que.popleft()
        if board[y][x] == "G":
            return cnt
                
        for ny,nx in get_direction(y,x,board):
            if not visited[ny][nx]:
                visited[ny][nx] = True
                que.append((ny,nx,cnt + 1))
                    
    return -1
            
        
    