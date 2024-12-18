def main(n):
    dp = [0, 0, 1, 1, 2]
    for i in range(n + 1):
        if i < len(dp):
            continue
        a = dp[-1]
        b = dp[i // 3] if i % 3 == 0 else float('inf')
        c = dp[i // 2] if i % 2 == 0 else float('inf')
        dp.append(min(a,b,c) + 1)
        
    return dp[n]


n = int(input())
print(main(n))   
    