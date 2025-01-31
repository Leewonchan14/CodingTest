import sys

input = sys.stdin.readline

def min_cost_to_merge(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]  # DP 배열
    prefix_sum = [0] * (n + 1)  # 누적합 배열

    # 누적합 계산 (prefix_sum[i] = arr[0] + ... + arr[i-1])
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    # DP 테이블 채우기
    for length in range(2, n + 1):  # 부분 구간 크기 2 이상부터 시작
        for l in range(n - length + 1):
            r = l + length - 1
            dp[l][r] = float('inf')
            # 가능한 모든 분할 지점 탐색
            for mid in range(l, r):
                dp[l][r] = min(dp[l][r], dp[l][mid] + dp[mid + 1][r])
            # 최소 비용 + 현재 구간 합
            dp[l][r] += prefix_sum[r + 1] - prefix_sum[l]

    print(dp[0][n - 1])  # 전체 합치기 비용 출력


tc = int(input())
for _ in range(tc):
    int(input())  # 파일 개수 (사용하지 않음)
    arr = list(map(int, input().split()))
    min_cost_to_merge(arr)