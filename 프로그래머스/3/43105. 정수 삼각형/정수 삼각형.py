"""
1. 아이디어
    - DP를 이용해 각 노드의 최댓값을 갱신하며 최댓값만 나오게 코드를 작성한다.

2. 시간 복잡도
    -  1 + 2 + 3 + ... + n  으로 n**2 복잡도가 나올것 같다.
    - n의 최대가 500이므로 250000(25만) < 20억 이므로
    - 가능

3. 자료 구조
    - 실제 삼각 배열 = int[][]
    - dp = (실제 삼각 배열과 같은) int[][]

"""


def solution(triangle):
    dp = [[0] * len(item) for item in triangle]
    max_height = len(triangle)

    dp[0][0] = triangle[0][0]

    height = 1
    while height < max_height:
        for index, item in enumerate(triangle[height]):
            if index != len(triangle[height]) - 1:
                dp[height][index] = max(dp[height][index], dp[height - 1][index] + item)
            if index != 0:
                dp[height][index] = max(dp[height][index], dp[height - 1][index - 1] + item)

        height += 1

    return max(dp[-1])
