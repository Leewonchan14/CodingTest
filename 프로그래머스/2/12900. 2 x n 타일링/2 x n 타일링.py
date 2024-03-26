"""
1. 아이디어
    - 점화식을 이용한 DP 풀이를 이용한다.
    - 특정 K일때 갯수는 k-1 + k-2 * 2 - (중복)k-2 인 점화식을 이용한다.
    - n(k) = n(k-1) + n(k-2) * 2 - n(k-2) == n(k-1) + n(k-2)

2. 시간 복잡도
    - 결국 계산은 n 번 하게 된다.
    - n 은 60000 이하이므로 20억이하 이다.
    - 가능

3. 자료구조
    - dp = int[][]
"""


def solution(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    if n <= 3:
        return dp[n]

    for i in range(4, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    return dp[-1]
