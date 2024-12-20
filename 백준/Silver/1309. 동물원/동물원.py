def main(n):
    dp = [[], [1,1,1]]
    for i in range(len(dp), n + 1):
        a = (dp[-1][1] + dp[-1][2]) % 9901
        b = (dp[-1][0] + dp[-1][2]) % 9901
        c = sum(dp[-1]) % 9901
        dp.append([a,b,c])
        
    return sum(dp[n]) % 9901

import sys

input = sys.stdin.readline

n = int(input())
print(main(n))