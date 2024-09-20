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
    dp = [triangle[0]]
    for h in range(1, len(triangle)):
        dp.append([])
        for w in range(h + 1):
            top = None
            if 0 < w < h:
                top = max(dp[h - 1][w - 1], dp[h - 1][w])
            else:
                top = dp[h - 1][w] if w == 0 else dp[h - 1][w - 1]
                
            dp[h].append(top + triangle[h][w])
                
        
    
    return max(dp[-1])
                
    
