def solution(board):
    dr = [-1 , 0 , -1]
    dc = [0, -1, -1]
    rows = len(board)
    columns = len(board[0])
    maxv = max(0, board[0][0])
    for r in range(1, rows):
        for c in range(1, columns):
            if board[r][c] == 1:
                    
                minv = min([board[r + dr[i]][c + dc[i]] for i in range(3)])
                board[r][c] = minv + 1

            maxv = max(board[r][c],maxv)
                
    return maxv ** 2
                