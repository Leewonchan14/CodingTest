import sys

sys.setrecursionlimit(10**6)  # 재귀 한도를 크게 설정

dp = {1: 1, 2: 1, 3: 2, 4: 1, 5: 2, 6: 2}

def recursion(k, n):
    if n in dp:
        return dp[n]
    
    if n % 2 == 0:
        return recursion(k, n // 2)
    
    dp[n] = recursion(k, n // 2) + 1
    
    return dp[n]

def solution(n):
    return recursion(0, n)