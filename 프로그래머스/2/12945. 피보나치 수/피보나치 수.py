import sys
sys.setrecursionlimit(10 ** 6) 


dp = {}

def fibo(n):
    if n <= 1:
        return n
    
    if n not in dp:
        dp[n] = (fibo(n - 2) + fibo(n - 1)) % 1234567
    
    return dp[n]

def solution(n):
    return fibo(n)
    