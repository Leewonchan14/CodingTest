import sys

input = sys.stdin.readline


def main(dp):
    for i in range(1, len(dp)):
        for j in range(3):
            dp[i][j] = min([dp[i - 1][k] for k in range(3) if k != j]) + dp[i][j]
            
    return min(dp[-1])

dp = [[int(i) for i in input().split()] for _ in range(int(input()))]
print(main(dp))