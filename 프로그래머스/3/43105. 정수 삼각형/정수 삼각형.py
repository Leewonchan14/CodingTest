def solution(triangle):
    dp = [[0] * len(i) for i in triangle]
    dp[0][0] = triangle[0][0]
    
    for h in range(1, len(triangle)):
        for w in range(len(triangle[h])):
            if w == h:
                dp[h][w] = dp[h - 1][w - 1] + triangle[h][w]
                continue
                
            if w == 0:
                dp[h][w] = dp[h - 1][w] + triangle[h][w]
                continue
            
            dp[h][w] = max(dp[h - 1][w - 1], dp[h - 1][w]) + triangle[h][w]
            
    return max(dp[-1])