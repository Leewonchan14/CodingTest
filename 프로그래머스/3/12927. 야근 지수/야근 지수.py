"""
야근 피로도 = sum(모든 남은일 작업량 ** 2)

야근 피로도 최소화값 리턴

1. 아이디어
    - 작업량을 우선순위 큐에 집어넣어 작업량이 많이 남은거부터 처리한다.

2. 시간복잡도
    - 20000 for 문 => 20000 +
    - 우선순위큐 삽입 => Sigma k 1~2000 log(k) => +
    - n번의 우선순위 큐에서 꺼내기, 삽입 => 1000000 * log(20000) +
    - 모든 작업량 접근후 제곱후 합연산 => 20000
    - 20000 + 10000 + 40000000 + 40000
    = 40070000
    가능
    
3. 자료구조
    - 우선순위큐 que :PriorityQueue

"""

def solution(n, works):
    count = [0] * 50001
    
    maxv = -1

    for w in works:
        maxv = max(maxv, w)
        count[w] += 1
        
    while n > 0:
        n -= 1
        count[maxv] -= 1
        count[maxv - 1] += 1
        if count[maxv] == 0:
            maxv -= 1
            if maxv == 0:
                break
    
    return sum([(i ** 2) * v for i, v in enumerate(count) if v != 0])
    

    
        

    return sum([i ** 2 for i in que.queue])

