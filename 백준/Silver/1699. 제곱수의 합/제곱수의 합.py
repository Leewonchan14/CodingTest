import sys

input = sys.stdin.readline

def preNum(n):
    li = [0]
    i = 1
    while i ** 2 <= n:
        li.append(i ** 2)
        i += 1
        
    return li

def main(n):
    nums = preNum(n)
    dp = [0, 1]
    for i in range(2, n + 1):
        if int(i ** 0.5) ** 2 == i:
            dp.append(1)
            continue
        dp.append(min([dp[i - j] + 1 for j in nums if j < i and j != 0]))
        
    return dp[n]
        
    

        
    
    

n = int(input())
print(main(n))