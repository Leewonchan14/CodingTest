def main(n):
    dp = [0, 1, 2]
    for i in range(n + 1):
        if i < len(dp):
            continue
            
        dp.append((dp[-1] + dp[-2]) % 10007)
        
    return dp[n]

print(main(int(input())))