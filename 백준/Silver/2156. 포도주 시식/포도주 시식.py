import sys


def main(arr):
    maxv = max(arr)
    dp = [[0] * 3 for _ in range(len(arr))]
    dp[0][1], dp[0][2] = (arr[0], arr[0])

    for i in range(1, len(arr)):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = dp[i - 1][0] + arr[i]
        dp[i][2] = dp[i - 1][1] + arr[i]

        maxv = max(maxv, max(dp[i]))

    return maxv


input = sys.stdin.readline

tc = int(input())
arr = [int(input()) for _ in range(tc)]
print(main(arr))
