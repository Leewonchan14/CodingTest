def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    
    dp[0][0] = 1
    
    for w,h in puddles:
        dp[h - 1][w - 1] = -1
        
    for h in range(n):
        for w in range(m):
            if h == 0 and w == 0:
                continue
            
            if dp[h][w] == -1:
                dp[h][w] = 0
                continue
                
            if h == 0:
                dp[h][w] = dp[h][w - 1]
                continue
                
            if w == 0:
                dp[h][w] = dp[h - 1][w]
                continue
            
            
            dp[h][w] = (dp[h - 1][w] + dp[h][w - 1]) %  1000000007
            
            
    return dp[-1][-1]