n = int(input())

dp = []
for _ in range(n):
    w, h = [int(i) for i in input().split()]
    dp.append([w, h, 0])
    
for i in range(len(dp) - 1):
    for j in range(i + 1, len(dp)):
        if dp[i][0] < dp[j][0] and dp[i][1] < dp[j][1]:
            dp[i][2] += 1
        elif dp[i][0] > dp[j][0] and dp[i][1] > dp[j][1]:
            dp[j][2] += 1
            
print(*[i[2] + 1 for i in dp])
    

