import sys

input = sys.stdin.readline


def main(arr):
    dp = [1] * len(arr)
    for i in range(len(arr)):
        pre = [dp[j] for j in range(i) if arr[j] < arr[i]]
        dp[i] = max(pre if pre else [0]) + 1
    return max(dp)


input()
arr = [int(i) for i in input().split()]
print(main(arr))
