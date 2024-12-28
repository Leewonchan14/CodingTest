import sys

input = sys.stdin.readline

tc= int(input())

arr = [int(input()) for _ in range(tc)]

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

def solve(n):
    for i in range(len(dp), n + 1):
        dp.append(dp[-1] + dp[-5])
        
    return dp[n]
        

def main():
    for a in arr:
        print(solve(a))

main()
    