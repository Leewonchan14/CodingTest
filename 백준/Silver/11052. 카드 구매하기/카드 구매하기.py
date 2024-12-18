def main(arr):
    dp = [0] * (len(arr) + 2)

    for i in range(1, len(arr) + 1):
        dp[i] = max(arr[i - 1], dp[i])
        for j in range(i + 1, len(arr) + 1):
            dp[j] = max(dp[j - i] + dp[i], dp[j])

    return dp[len(arr)]


n = int(input())
arr = [int(i) for i in input().split()]
print(main(arr))
