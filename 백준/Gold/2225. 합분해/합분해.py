def main(n, k):
    dp = [([1] * (n + 1)) for _ in range(k + 1)]
    for kk in range(2, k + 1):
        for nn in range(1, n + 1):
            dp[kk][nn] = (dp[kk - 1][nn] + dp[kk][nn - 1]) % 1000000000
            
    return dp[k][n]

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

print(main(n, k))