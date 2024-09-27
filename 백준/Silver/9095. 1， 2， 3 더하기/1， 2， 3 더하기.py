dp = [0, 1, 2, 4]


for _ in range(int(input())):
    n = int(input())
    for i in range(len(dp), n + 1):
        dp.append(dp[-1] + dp[-2] + dp[-3])
    print(dp[n])
