def longest_increasing_subsequence(n, arr):
    # DP 배열 초기화
    dp = [1] * n

    # DP 계산
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 결과 반환
    return max(dp)


# 입력
import sys

input = sys.stdin.readline
input()
data = input().split()
arr = [int(i) for i in data]

# 결과 출력
print(longest_increasing_subsequence(len(arr), arr))
