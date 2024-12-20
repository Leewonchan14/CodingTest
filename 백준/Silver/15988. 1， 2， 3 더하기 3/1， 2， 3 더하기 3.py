import sys

input = sys.stdin.readline

dp = [0, 1, 2, 4]
def get(n):
    if n < len(dp):
        return dp[n]
    
    for i in range(len(dp), n + 1):
        dp.append((dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009)
        
    return dp[n]

def main(arr):
    for i in arr:
        print(get(i))
     
arr = [int(input()) for i in range(int(input()))]
main(arr)