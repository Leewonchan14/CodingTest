import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = [int(i) for i in input().split()]

dp = [arr[0]]
for i in range(1, n):
    dp.append(dp[-1] + arr[i])
    
for _ in range(m):
    a,b = map(int, input().split())
    result = dp[b - 1] - (dp[a - 2] if a - 2 >= 0 else 0)
    print(result)
    