import sys
sys.setrecursionlimit(10 ** 9)

dp = [0, 1, 2]

def recursive(n):
    for i in range(n + 1):
        if i < len(dp):
            continue
        dp.append((dp[-1] + dp[-2]) % 1234567)
    return dp[n]
        

def solution(n):
    return recursive(n)