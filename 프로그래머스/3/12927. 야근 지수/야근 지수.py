"""
야근 피로도 = sum(모든 남은일 작업량 ** 2)

야근 피로도 최소화값 리턴

1. 아이디어
    - 작업량을 카운트 정렬로 정렬후 뒤에서 하나씩 빼다가 마지막에 제곱수를 더해준다.

2. 시간복잡도
    - 카운트 정렬 20000 for 문 => 20000 +
    - n번의 작업 => 1000000
    - 모든 작업량 접근후 제곱후 합연산 => 20000
    - 20000 + 1000000 + 20000
    = 1040000
    가능

3. 자료구조
    - 카운트정렬 count : int[]

"""


def solution(n, works):
    count = [0] * 50001
    
    max_idx = 50000
    
    for w in works:
        count[w] += 1
        
    while n > 0:
        while count[max_idx] == 0 and max_idx >= 0:
            max_idx -= 1
            
        if max_idx < 0:
            break
        
        n -= 1
        count[max_idx] -= 1
        if max_idx > 0:
            count[max_idx - 1] += 1
        
    print([(i ** 2) * v for i,v in enumerate(count) if not v == 0])
    
    return sum([(i ** 2) * v for i,v in enumerate(count)])
        
        
            
