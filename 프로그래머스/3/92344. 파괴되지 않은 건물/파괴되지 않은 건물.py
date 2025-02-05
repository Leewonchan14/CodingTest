def solution(board, skill):
    dp = [([0] * (len(board[0]) + 1)) for _ in range(len(board) + 1)]
    for t, r1, c1, r2, c2, d in skill:
        boo = -d if t == 1 else d
        r2 += 1
        c2 += 1
        dp[r1][c1] += boo
        dp[r2][c2] += boo
        dp[r1][c2] -= boo
        dp[r2][c1] -= boo
        
    for r in range(1, len(board)):
        for c in range(len(board[0])):
            dp[r][c] += dp[r - 1][c]
            
    for c in range(1, len(board[0])):
        for r in range(len(board)):
            dp[r][c] += dp[r][c - 1]
            
            
    cnt = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] + dp[r][c] >= 1:
                cnt += 1
                
    return cnt
                
    