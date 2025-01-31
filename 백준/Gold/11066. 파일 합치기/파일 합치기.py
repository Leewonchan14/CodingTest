import sys

def main(arr):
    n = len(arr)
    if n == 0:
        print(0)
        return
    
    # 누적 합 배열 생성
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    
    # DP 및 최적 분기점 저장 배열 초기화
    dp = [[0]*n for _ in range(n)]
    opt = [[0]*n for _ in range(n)]
    
    for i in range(n):
        opt[i][i] = i  # 길이 1인 구간 초기화
    
    # 구간 길이 2부터 시작
    for length in range(2, n+1):
        for l in range(n - length + 1):
            r = l + length - 1
            dp[l][r] = float('inf')
            
            # 최적 분기점 범위 설정
            kl = opt[l][r-1] if l < r-1 else l
            kr = opt[l+1][r] if l+1 < r else r-1
            
            # 최적 분기점 탐색
            for k in range(kl, kr+1):
                current = dp[l][k] + dp[k+1][r] + (prefix[r+1] - prefix[l])
                if current < dp[l][r]:
                    dp[l][r] = current
                    opt[l][r] = k
    
    print(dp[0][n-1])

# 입력 처리
input = sys.stdin.readline
tc = int(input())
for _ in range(tc):
    input()  # 배열 크기 입력 건너뛰기
    arr = list(map(int, input().split()))
    main(arr)