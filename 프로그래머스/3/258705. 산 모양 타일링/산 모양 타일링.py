"""
1. 아이디어
    - dp를 이용하여 위로 붙은 삼각형일때 경우와 아래만 붙은 삼각형일때 를 다르게 계산하여 계속 구한다.
    - 맨 오른쪽 아래가 없는 것과 있는것을 나뉘어 dp를 계산한다.
        
2. 시간 복잡도
    - 100000만큼 실행된다.
    - 가능
    
3. 자료구조
    - dp : int[][]
"""

dp = []


def solution(n, tops):
    if tops[0] == 1:
        dp.append([3, 4])
    else:
        dp.append([2, 3])

    for i in range(1, n):
        if tops[i] == 1:
            a = dp[-1][1] * 2 + dp[-1][0]
            b = dp[-1][1] * 3 + dp[-1][0]
            dp.append([a % 10007, b % 10007])
        else:
            a = dp[-1][0] + dp[-1][1]
            b = dp[-1][1] * 2 + dp[-1][0]
            dp.append([a % 10007, b % 10007])

    return dp[-1][1]

