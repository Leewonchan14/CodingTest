def getMin(y, x, dp):
    return min(dp[y - 1][x], dp[y][x  - 1], dp[y - 1][x - 1])
    

def solution(board):
    dp = [[0] * (len(board[0]) + 1) for r in range(len(board) + 1)]
    for r in range(1, len(dp)):
        for c in range(1, len(dp[r])):
            if board[r - 1][c - 1] == 0:
                continue
                
            dp[r][c] = getMin(r, c, dp) + 1
            
    return max([max(i) for i in dp]) ** 2
    
            