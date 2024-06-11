def solution(n, money):
    money.sort()
    dp = [0] * (n + 1)
    
    for m in money:
        dp[m] += 1
        for i in range(1 , n + 1):
            if i - m >= 0:
                dp[i] += dp[i - m];
        
    return dp[-1]