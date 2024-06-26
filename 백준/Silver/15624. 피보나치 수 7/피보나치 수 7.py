import sys
input = sys.stdin.readline

dp = [0, 1, 1]

N = int(input())

def fibo(n):
    if n < len(dp):
        return dp[n]
    
    for i in range(3, n + 1):
        dp.append((dp[-1] + dp[-2]) % 1000000007)
    
    return dp[n]
    

print(fibo(N))
    