def main(arr):
    dp = [[0, 0] for _ in range(len(arr))]

    dp[0][0] = arr[0]

    maxv = arr[0]

    for i in range(1, len(arr)):
        dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
        dp[i][1] = max(dp[i - 1][1] + arr[i], dp[i - 1][0])

        maxv = max(maxv, max(dp[i][0], dp[i][1]))

    return maxv


import sys

input = sys.stdin.readline

input()
arr = [int(i) for i in input().split()]
print(main(arr))
