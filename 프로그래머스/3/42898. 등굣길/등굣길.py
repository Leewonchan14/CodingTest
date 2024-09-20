"""
1. 아이디어
    - 오른쪽과 아래 밖에 가지 못하므로 해당하는 좌표에 갈수있는 경우의 수는 왼쪽 + 위쪽이다.
    - 모든 좌표를 2중for문으로 돌며 왼쪽+위쪽 경우의수를 더한다
    
2. 시간 복잡도
    - m x n 2차원 배열을 도는 O(n*m)으로
    - 100 * 100 => 10000 
    - 가능
    
3. 자료구조
    - dp: int[][] == 동적 경우의수를 담을 2차원 배열
"""

def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
#     for i in range(m + 1):
#         dp[0][i] = 1
        
#     for i in range(n + 1):
#         dp[i][0] = 1
    
    
    dic = {}
    
    for a, b in puddles:
        dic[b,a] = True
    
        
    for h in range(1, n + 1):
        for w in range(1, m + 1):
            if h == 1 and w == 1:
                dp[h][w] = 1
                continue
                
            dp[h][w] = (dp[h - 1][w] + dp[h][w - 1]) % 1000000007
            
            if (h, w) in dic:
                dp[h][w] = 0
                
    return dp[-1][-1]
            
    
            
    