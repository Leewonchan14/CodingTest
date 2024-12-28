import sys

input = sys.stdin.readline

n = int(input())

def main():
    dp = [0, 1, 2, 3, 5]
    for i in range(len(dp), n + 1):
        dp.append((dp[-1] + dp[-2]) % 15746)
    print(dp[n])

main()
