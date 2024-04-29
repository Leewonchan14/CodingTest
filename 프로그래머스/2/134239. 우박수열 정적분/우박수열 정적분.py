def solution(k, ranges):
    dp = [0]
    while k != 1:
        if k % 2 == 0:
            n_k = k // 2
        else:
            n_k = k * 3 + 1
        dp.append(dp[-1] + n_k + k)
        
        k = n_k
        
    n = len(dp) - 1
    result = []
    for a,b in ranges:
        c = n + b
        if a > n or c > n or c < a:
            result.append(-1)
        else:
            result.append((dp[c] - dp[a]) / 2)
        
    return result
        