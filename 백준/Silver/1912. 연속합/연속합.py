import sys

input = sys.stdin.readline

def main(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])
        
    return max(dp)

input()
arr = [int(i) for i in input().split()]
print(main(arr))