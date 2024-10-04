def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    dp[1][1] = 1
    
    for w,h in puddles:
        dp[h][w] = -1
        
    for h in range(1, n + 1):
        for w in range(1, m + 1):
            if h == 1 and w == 1:
                continue
            
            if dp[h][w] == -1:
                dp[h][w] = 0
                continue
                
            dp[h][w] = (dp[h - 1][w] + dp[h][w - 1]) %  1000000007
            
            
    return dp[-1][-1]