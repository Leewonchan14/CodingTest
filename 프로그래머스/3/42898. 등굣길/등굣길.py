def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n+1)]
    pud = [[False] * (m + 1) for _ in range(n+1)]
    dp[0][1] = 1
    
    for column,row in puddles:
        pud[row][column] = True
    
    for row in range(1, n + 1):
        for column in range(1, m + 1):
            dp[row][column] = (dp[row - 1][column] + dp[row][column - 1]) % 1000000007
            
            if pud[row][column]:
                dp[row][column] = 0
    
    return dp[n][m]
    
        