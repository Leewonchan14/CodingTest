def solution(board):
    dp = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    _max = 0
    
    for row in range(1, len(board) + 1):
        for col in range(1, len(board[0]) + 1):
            if board[row-1][col-1] == 0:
                continue
            
            left = dp[row][col - 1]
            up = dp[row - 1][col]
            cross = dp[row - 1][col - 1]
            
            dp[row][col] = min([left, up, cross]) + board[row-1][col-1]
            
            if dp[row][col] > _max :
                _max = dp[row][col]
    return _max**2