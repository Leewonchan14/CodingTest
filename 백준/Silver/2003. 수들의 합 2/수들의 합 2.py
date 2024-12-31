import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = [int(i) for i in input().split()]

def main():
    dp = [0]
    for i in range(len(arr)):
        dp.append(dp[-1] + arr[i])
        
    cnt = 0
    for i in range(1, len(dp)):
        for j in range(0, i):
            if dp[i] - dp[j] == m:
                cnt += 1
                
    return cnt
            

print(main())