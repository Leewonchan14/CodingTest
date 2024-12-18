def main(n):
    dp = [[], [0, 1], [1, 0]]
    for i in range(len(dp), n + 1):
        a = sum(dp[-1])
        b = dp[-1][0]
        dp.append([a, b])
        
    return sum(dp[n])

n = int(input())
print(main(n))