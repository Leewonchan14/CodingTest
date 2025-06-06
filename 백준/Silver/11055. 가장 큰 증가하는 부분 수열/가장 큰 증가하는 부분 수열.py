def main(arr):
    dp = [arr[i] for i in range(len(arr))]
    for i in range(len(arr)):
        pre = [dp[j] for j in range(i) if arr[j] < arr[i]]
        dp[i] += max(pre) if pre else 0
        
    return max(dp)
        


import sys

input = sys.stdin.readline

input()
arr = [int(i) for i in input().split()]
print(main(arr))