n = int(input())

dp = [0, 1, 2, 3, 4, 5, 6]


def main():  
    while len(dp) <= n:
        # 1. A한번 더쓰기
        v1 = dp[-1] + 1
        # 2. 3단계 전 복붙
        v2 = dp[-3] * 2
        # 3. 4단계 전 복붙
        v3 = dp[-4] * 3
        # 4. 5단계 전의 버퍼 복붙
        v4 = dp[-5] * 4
        # 5. 6단계 전의 버퍼 복붙
        v5 = dp[-6] * 5
        
        dp.append(max([v1, v2, v3, v4, v5]))
        
    return dp[n]

print(main())