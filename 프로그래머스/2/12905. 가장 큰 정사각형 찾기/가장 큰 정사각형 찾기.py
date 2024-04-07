def solution(board):
    dr = [-1 , 0 , -1]
    dc = [0, -1, -1]
    rows = len(board)
    columns = len(board[0])
    maxv = 0
    for r in range(rows):
        for c in range(columns):
            if board[r][c] == 1:
                ls = []
                for i in range(3):
                    if 0<= (r + dr[i]) < rows and 0 <= (c + dc[i]) < columns:
                        ls.append(board[r + dr[i]][c + dc[i]])
                    else:
                        ls.append(0)
                board[r][c] = min(ls) + 1
                maxv = max(maxv , board[r][c])
                
    return maxv ** 2
                