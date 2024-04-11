def solution(board, h, w):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    target = board[h][w]
    cnt = 0
    for i in range(4):
        ny = h + dy[i]
        nx = w + dx[i]
        if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] == target: 
            cnt += 1
            
    return cnt